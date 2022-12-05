import 'dart:convert';
import 'dart:io';
import 'package:image_picker/image_picker.dart';

import 'variables.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'profile.dart';
import 'package:http/http.dart' as http;
import 'dart:core';


class ArtItem extends StatefulWidget {
  ArtItem({
    Key? key,
    required this.id,
    required this.title,
    required this.description,
    required this.owner,
    required this.type,
    required this.tags,
    required this.artitem_path,
  });
  final int id;
  final String title;
  final String description;
  final String owner;
  final String type;
  final String tags;
  final String artitem_path;
  @override
  State<ArtItem> createState() => _ArtItemState();
}

class _ArtItemState extends State<ArtItem> {
  @override
  Widget build(BuildContext context) {
    return Container();
  }
}

Future<ArtItem> getAllArtItems() async {
  final response = await http.get(
      Uri.parse(GET_ALL_ART_ITEM_ENDPOINT+"1"),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': 'Token $token'

      }
  );
  print(response.statusCode) ;
  print(response.body) ;

  Map<String, dynamic> body = jsonDecode(response.body);

  if (response.statusCode == 200) {
    ArtItem x = ArtItem(id: body["id"], title: body["title"], description: body["description"], owner: "Suleyman Cakir", type: body["type"], tags: "AA", artitem_path: body["artitem_path"]) ;
    print(x.description);
    print(x.id);
    print(x.title);
    return x;
  }
  return  ArtItem(id: body["id"], title: "ERROR", description:"ERROR", owner: "ERROR", type: "ERROR", tags:"ERROR", artitem_path: "ERROR");

}
Future<String> uploadArtItem(title, description, String tags, XFile? image) async {
  List<String> tagArray = tags.split(',') ;
  String base64Image = '"data:image/jpeg;base64,' ;
  if (image != null) {
  File(image.path).readAsBytes().then((value) async {

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





