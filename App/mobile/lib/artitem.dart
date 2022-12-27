import 'dart:convert';
import 'dart:io';
import 'package:image_picker/image_picker.dart';

import 'variables.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'profile.dart';
import 'package:http/http.dart' as http;
import 'dart:core';
import 'package:flutter_native_image/flutter_native_image.dart';

import 'getimage.dart';


class ArtItem extends StatefulWidget {
  ArtItem({
    Key? key,
    required this.id,
    required this.title,
    required this.description,
    required this.username,
    required this.tags,
    required this.artitem_path,
    required this.profile_path,
    required this.likes,
  });
  final int id;
  final String title;
  final String description;
  final String username;
  final List<dynamic> tags;
  final String artitem_path;
  final String profile_path;
  final int likes;
  

  @override
  State<ArtItem> createState() => _ArtItemState();
}
class ArtItemUserClass{

      int id;
      String username;
      String name;
      String surname;
      String profile_path;
  
      ArtItemUserClass(this.id,this.username,this.name, this.surname,this.profile_path) ;
    factory ArtItemUserClass.fromJson(dynamic json) {
    return ArtItemUserClass(json['id'], json['username'],json['name'], json['surname'],json['profile_path']);
  }
    }
class _ArtItemState extends State<ArtItem> {
  @override
  Widget build(BuildContext context) {
    return Container();
  }
}

Future <List<ArtItem>> getAllArtItems() async {
  final response = await http.get(
      Uri.parse(GET_ALL_ART_ITEM_ENDPOINT),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': 'Token $token'

      }
  );
  //print(response.statusCode) ;
  print(response.body) ;

List <dynamic> items = jsonDecode(response.body);
  List <ArtItem> userArtItems = [] ;
  if (response.statusCode == 200) {
    for (var body in items) {
    ArtItemUserClass owner = ArtItemUserClass.fromJson(body['owner']);
    String profileUrl = await getImage(owner.profile_path) ;

    String itemURL = await getImage(body['artitem_path']) ;
    print(itemURL);

    //Profile profile = await getOtherProfile(owner.id);
    ArtItem x = ArtItem(id: body["id"], title: body["title"], description: body["description"], username: owner.username,  tags: body["tags"], artitem_path: itemURL,profile_path: profileUrl, likes : body["likes"]) ;
    //print(x.description);
    //print(x.id);
    print(x.title);
    print("Finished") ;
    userArtItems.add(x);
  }
  }
  print(userArtItems);
  return userArtItems ;
}
Future <List<ArtItem>> getuserArtItems() async {
  print("started") ;
  final response = await http.get(
      Uri.parse(GET_USER_ART_ITEM_ENDPOINT),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': 'Token $token'

      }
  );
  //print(response.statusCode) ;
  //print(response.body) ;

  List <dynamic> items = jsonDecode(response.body);
  List <ArtItem> userArtItems = [] ;
  if (response.statusCode == 200) {
    for (var body in items) {
    ArtItemUserClass owner = ArtItemUserClass.fromJson(body['owner']);
    //print(owner);
    String itemURL = await getImage(body['artitem_path']) ;
try{
    ArtItem x = ArtItem(id: body["id"], title: body["title"], description: body["description"], username: owner.username,  tags: body["tags"], artitem_path: itemURL, profile_path: "", likes: body["likes"]) ;
    userArtItems.add(x);

}
catch (e){
  print(e) ;
}
    //print(x.description);
    //print(x.id);
    //print(x.title);
  }
  }
  print(userArtItems);
  print("returned");
  return userArtItems ;

}
Future<String> uploadArtItem(title, description, String tags, XFile? image) async {
  List<String> tagArray = tags.split(',') ;
  String base64Image = '"data:image/jpeg;base64,' ;
  if (image != null) {
      File compimage =    (await FlutterNativeImage.compressImage(image.path,
        quality: 25));
  File(compimage.path).readAsBytes().then((value) async {

   base64Image = base64Image +   base64Encode(value);
    final response = await http.post(
      Uri.parse(UPLOAD_ART_ITEM_ENDPOINT),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': 'Token $token'

      } ,
      body: jsonEncode(<String, dynamic>{
      'title': title,
      'description' : description,
      'type' : "Sketch",
      'tags' : [],
      "artitem_image": base64Image,
    })
  );
  print(response.statusCode) ;
  print(response.body) ;


  if (response.statusCode == 201) {

    return  "OK";
  }
  return  "response.body" ;


 
}) ;
  }
     
    return "not ok." ;
   
}

Future<String> likeArtItem(int id) async {
    String strid = id.toString();
    String LIKE_ART_ITEM_ENDPOINT = "http://$HOST/api/v1/users/artitems/$strid/unlike/"  ;
    final response = await http.delete(
      Uri.parse(LIKE_ART_ITEM_ENDPOINT),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': 'Token $token'

      } ,
      );
  print(response.statusCode) ;
  print(response.body) ;


  if (response.statusCode == 204) {

    return  "unliked";
  }
  else {
    LIKE_ART_ITEM_ENDPOINT = "http://$HOST/api/v1/users/artitems/$strid/like/"  ;
    final response = await http.post(
      Uri.parse(LIKE_ART_ITEM_ENDPOINT),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': 'Token $token'

      } ,
      );
        print(response.statusCode) ;
  print(response.body) ;
  }
  return  "liked" ;


 
}


Future <List<ArtItem>> searchArtItems(String search) async {
  final response = await http.get(
      Uri.parse(SEARCH_ART_ITEM_ENDPOINT+"?search=$search"),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': 'Token $token'

      }
  
  );
  
  //print(response.statusCode) ;
  print(response.body) ;

List <dynamic> items = jsonDecode(response.body);
  List <ArtItem> userArtItems = [] ;
  if (response.statusCode == 200) {
    for (var body in items) {
    ArtItemUserClass owner = ArtItemUserClass.fromJson(body['owner']);
    String profileUrl = await getImage(owner.profile_path) ;

    String itemURL = await getImage(body['artitem_path']) ;
    print(itemURL);

    //Profile profile = await getOtherProfile(owner.id);
    ArtItem x = ArtItem(id: body["id"], title: body["title"], description: body["description"], username: owner.username,  tags: body["tags"], artitem_path: itemURL,profile_path: profileUrl, likes : body["likes"]) ;
    //print(x.description);
    //print(x.id);
    print(x.title);
    print("Finished") ;
    userArtItems.add(x);
  }
  }
  print(userArtItems);
  return userArtItems ;
}
