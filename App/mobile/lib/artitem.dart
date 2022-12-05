import 'dart:convert';
import 'package:artopia/variables.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:artopia/profile.dart';
import 'package:http/http.dart' as http;
import 'dart:core';

import 'getimage.dart';


class ArtItem extends StatefulWidget {
  ArtItem({
    Key? key,
    required this.id,
    required this.title,
    required this.description,
    required this.username,
    required this.type,
    required this.tags,
    required this.artitem_path,
    required this.profile_path,
  });
  final int id;
  final String title;
  final String description;
  final String username;
  final String type;
  final String tags;
  final String artitem_path;
  final String profile_path;
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
 // print(response.statusCode) ;
 // print(response.body) ;

List <dynamic> items = jsonDecode(response.body);
  List <ArtItem> userArtItems = [] ;
  if (response.statusCode == 200) {
    for (var body in items) {
    ArtItemUserClass owner = ArtItemUserClass.fromJson(body['owner']);
    print(owner);
    String itemURL = await getImage(body['artitem_path']) ;
    //Profile profile = await getOtherProfile(owner.id);
    ArtItem x = ArtItem(id: body["id"], title: body["title"], description: body["description"], username: owner.username, type: body["type"], tags: "", artitem_path: itemURL,profile_path: owner.profile_path) ;
    print(x.description);
    print(x.id);
    print(x.title);
    userArtItems.add(x);
  }
  }
  print(userArtItems);
  return userArtItems ;
}
Future <List<ArtItem>> getuserArtItems() async {
  final response = await http.get(
      Uri.parse(GET_USER_ART_ITEM_ENDPOINT),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': 'Token $token'

      }
  );
  print(response.statusCode) ;
  print(response.body) ;

  List <dynamic> items = jsonDecode(response.body);
  List <ArtItem> userArtItems = [] ;
  if (response.statusCode == 200) {
    for (var body in items) {
    ArtItemUserClass owner = ArtItemUserClass.fromJson(body['owner']);
    print(owner);
    String itemURL = await getImage(body['artitem_path']) ;

    ArtItem x = ArtItem(id: body["id"], title: body["title"], description: body["description"], username: owner.username, type: body["type"], tags: "AA", artitem_path: itemURL, profile_path: "",) ;
    print(x.description);
    print(x.id);
    print(x.title);
    userArtItems.add(x);
  }
  }
  print(userArtItems);
  return userArtItems ;

}





