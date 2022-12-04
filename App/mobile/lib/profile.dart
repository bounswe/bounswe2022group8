import 'package:artopia/getimage.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'dart:core';
import 'package:url_launcher/url_launcher.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'variables.dart' ;
class Profile extends StatefulWidget {
  Profile({
    required this.imageUrl,
    required this.username,
    required this.name,
    required this.bio,
    required this.location,
    required this.followers,
    required this.following,
  });
  final String imageUrl;
  final String username;
  final String name;
  final String bio;
  final String location;
  final int followers;
  final int following;

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
    return  Profile(bio: body["about"], followers: 0, following: 0, imageUrl: profileUrl, location: body["location"], name: body["name"], username: registered_username) ;
  }
return  Profile(bio: body["about"], followers: 0, following: 0, imageUrl: '', location: body["location"], name: "Error", username: "Error",)  ;  
  
}