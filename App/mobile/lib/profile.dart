import 'dart:io';

import 'package:image_picker/image_picker.dart';

import 'getimage.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'dart:core';
import 'package:url_launcher/url_launcher.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'variables.dart' ;
import 'package:flutter_native_image/flutter_native_image.dart';

class Profile extends StatefulWidget {
  Profile({
    required this.imageUrl,
    required this.username,
    required this.name,
    required this.bio,
    required this.location,
    required this.followers,
    required this.following,
    required this.id,
  });
  final String imageUrl;
  final String username;
  final String name;
  final String bio;
  final String location;
  final int followers;
  final int following;
  final int id;
  @override
  State<Profile> createState() => _ProfileState();
}

class _ProfileState extends State<Profile> {
  
  @override
  Widget build(BuildContext context) {
    final Uri imagelUrl = Uri.parse(widget.imageUrl);
    final Uri usernameUrl = Uri.parse(widget.username);
    final Uri nameUrl = Uri.parse(widget.name);
    final Uri bioUrl = Uri.parse(widget.bio);
    final Uri locationUrl = Uri.parse(widget.location);
    final Uri followersUrl = Uri.parse(widget.followers.toString());
    final Uri followingUrl = Uri.parse(widget.following.toString());
    void getUrlLauncher(Uri url) async {
      if (await canLaunchUrl(url)) {
        await launchUrl(url);
      } else {
        throw 'Could not launch $url';
      }
    }

    return Container();
  }
}

Future<Profile> getMyProfile() async {
  final response = await http.get(
    Uri.parse(GET_PROFILE_ENDPOINT),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
      'Authorization': 'Token ' + token 

    }
   )
   ;
  print(response.statusCode) ;
  print(response.body) ;      
  
  Map<String, dynamic> body = jsonDecode(response.body);
  
  if (response.statusCode == 200) {
    String profileUrl = await getImage(body['profile_path']) ;
    return  Profile(bio: body["about"], followers: body['followers'], following: body['followings'], imageUrl: profileUrl, location: body["location"], name: body["name"], username: registered_username,id : body["id"]) ;
  }
return  Profile(bio: body["about"], followers: 0, following: 0, imageUrl: '', location: body["location"], name: "Error", username: "Error",id : body["id"])  ;  
  
}

Future<Profile> getOtherProfile(int id) async {
  final response = await http.get(
    Uri.parse(GET_OTHER_PROFILE_ENDPOINT + id.toString()),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
      'Authorization': 'Token ' + token 

    }
   )
   ;
  print(response.statusCode) ;
  print(response.body) ;      
  
  Map<String, dynamic> body = jsonDecode(response.body);
  
  if (response.statusCode == 200) {
    String profileUrl = await getImage(body['profile_path']) ;
    return  Profile(bio: body["about"], followers: body['followers'], following: body['followings'], imageUrl: profileUrl, location: body["location"], name: body["name"], username: registered_username, id : body["id"]) ;
  }
return  Profile(bio: body["about"], followers: 0, following: 0, imageUrl: '', location: body["location"], name: "Error", username: "Error",id : body["id"])  ;  
  
}
Future<String> uploadProfile(name, surname, bio, location,  XFile? image) async {
  String base64Image = '"data:image/jpeg;base64,' ;
  if (image != null) {
    File compimage =    (await FlutterNativeImage.compressImage(image.path,
        quality: 20)) ;

  File(compimage.path).readAsBytes().then((value) async {

   base64Image = base64Image +   base64Encode(value);
   final response = await http.put(
      Uri.parse(UPDATE_PROFILE_ENDPOINT),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': 'Token $token'

      } ,
      body: jsonEncode(<String, dynamic>{
      'name': name,
      'surname' : surname,
      'about' : bio,
      'location' : location,
      "profile_image": base64Image,
    })
  );
  print(response.statusCode) ;
  print(response.body) ;
  print(base64Image) ;
  Map<String, dynamic> body = jsonDecode(response.body);

  if (response.statusCode == 200) {

    return  "OK";
  }
   
   else {
    return "not ok." ;
   }
  
  });
  
}
return "not ok." ;
}