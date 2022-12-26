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
import 'dart:math';

import 'getimage.dart';

Future <String> postAnnotation(int startpoint, int endpoint, String annotation, String description) async {
  Profile me = await getMyProfile() ;
  String url = await getImage(annotated_item_url);
  const _chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz1234567890';
  Random _rnd = Random();

  String getRandomString(int length) => String.fromCharCodes(Iterable.generate(
    length, (_) => _chars.codeUnitAt(_rnd.nextInt(_chars.length))));
  final response = await http.post(
      Uri.parse(POST_ANNOTATIONS),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': 'Token $token'
      },  
      body: jsonEncode(<String, dynamic>{
           "@context": "http://www.w3.org/ns/anno.jsonld",
            "type": "Annotation",
            "body": [
        {
            "type": "TextualBody",
            "value": annotation, //changed
            "purpose": "commenting",
            "creator": { //changed
                "id": me.id,
                "name": me.username, 
            },
            "created": "2022-12-25T09:58:14.525Z", //dokunma
            "modified": "2022-12-25T09:58:15.130Z" //dokunma
        } 
    ],
    "target": {
        "selector": [
            {
                "type": "TextQuoteSelector", 
                "exact": description.substring(startpoint,endpoint) //changed
            },
            {
                "type": "TextPositionSelector",
                "start": startpoint, //changed
                "end": endpoint //changed
            }
        ],
        "source": url //changed
    },
    "id": getRandomString(35), // generated
    "creator": me.id //changed
    }) ,
  );
  print(response.statusCode) ;
  print(response.body) ;

  if (response.statusCode == 201) {
    return "OK";

  }
  else{
    return "not ok";
  }
}

Future <String> getAllAnnotations() async {
  
  final response = await http.get(
      Uri.parse(GET_TEXT_ANNOTATIONS+ annotated_item_id.toString()),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': 'Token $token'
      }, ); 
      
     
  print(response.statusCode) ;
  print(response.body) ;
  print(annotated_item_id);
  print("hola");
  Iterable l = json.decode(response.body);
  List<Body> bodies = (json.decode(response.body) as List).map((i) =>
              Body.fromJson(i)).toList();
  print(bodies[0]) ;
  if (response.statusCode == 200) {
    return "OK";

  }
  else{
    return "not ok";
  }
}
class Test {
  String? id;
  List<Body>? body;
  String? type;
  Target? target;
  int? creator;
  String? context;

  Test(
      {this.id, this.body, this.type, this.target, this.creator, this.context});

  Test.fromJson(Map<String, dynamic> json) {
    id = json['id'];
    if (json['body'] != null) {
      body = <Body>[];
      json['body'].forEach((v) {
        body!.add(new Body.fromJson(v));
      });
    }
    type = json['type'];
    target =
        json['target'] != null ? new Target.fromJson(json['target']) : null;
    creator = json['creator'];
    context = json['@context'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['id'] = this.id;
    if (this.body != null) {
      data['body'] = this.body!.map((v) => v.toJson()).toList();
    }
    data['type'] = this.type;
    if (this.target != null) {
      data['target'] = this.target!.toJson();
    }
    data['creator'] = this.creator;
    data['@context'] = this.context;
    return data;
  }
}

class Body {
  String? value;
  String? type;
  String? purpose;
  String? created;
  String? modified;
  Creator? creator;

  Body(
      {this.value,
      this.type,
      this.purpose,
      this.created,
      this.modified,
      this.creator});

  Body.fromJson(Map<String, dynamic> json) {
    value = json['value'];
    type = json['type'];
    purpose = json['purpose'];
    created = json['created'];
    modified = json['modified'];
    creator =
        json['creator'] != null ? new Creator.fromJson(json['creator']) : null;
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['value'] = this.value;
    data['type'] = this.type;
    data['purpose'] = this.purpose;
    data['created'] = this.created;
    data['modified'] = this.modified;
    if (this.creator != null) {
      data['creator'] = this.creator!.toJson();
    }
    return data;
  }
}

class Creator {
  int? id;
  String? name;

  Creator({this.id, this.name});

  Creator.fromJson(Map<String, dynamic> json) {
    id = json['id'];
    name = json['name'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['id'] = this.id;
    data['name'] = this.name;
    return data;
  }
}

class Target {
  String? id;
  String? source;
  String? type;
  List<Selector>? selector;

  Target({this.id, this.source, this.type, this.selector});

  Target.fromJson(Map<String, dynamic> json) {
    id = json['id'];
    source = json['source'];
    type = json['type'];
    if (json['selector'] != null) {
      selector = <Selector>[];
      json['selector'].forEach((v) {
        selector!.add(new Selector.fromJson(v));
      });
    }
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['id'] = this.id;
    data['source'] = this.source;
    data['type'] = this.type;
    if (this.selector != null) {
      data['selector'] = this.selector!.map((v) => v.toJson()).toList();
    }
    return data;
  }
}

class Selector {
  String? exact;
  String? type;
  int? start;
  int? end;

  Selector({this.exact, this.type, this.start, this.end});

  Selector.fromJson(Map<String, dynamic> json) {
    exact = json['exact'];
    type = json['type'];
    start = json['start'];
    end = json['end'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['exact'] = this.exact;
    data['type'] = this.type;
    data['start'] = this.start;
    data['end'] = this.end;
    return data;
  }
}
class Test1 {
  String? id;
  List<Body>? body;
  String? type;
  Target? target;
  int? creator;
  String? context;

  Test1(
      {this.id, this.body, this.type, this.target, this.creator, this.context});

  Test1.fromJson(Map<String, dynamic> json) {
    id = json['id'];
    if (json['body'] != null) {
      body = <Body>[];
      json['body'].forEach((v) {
        body!.add(new Body.fromJson(v));
      });
    }
    type = json['type'];
    target =
        json['target'] != null ? new Target.fromJson(json['target']) : null;
    creator = json['creator'];
    context = json['@context'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['id'] = this.id;
    if (this.body != null) {
      data['body'] = this.body!.map((v) => v.toJson()).toList();
    }
    data['type'] = this.type;
    if (this.target != null) {
      data['target'] = this.target!.toJson();
    }
    data['creator'] = this.creator;
    data['@context'] = this.context;
    return data;
  }
}

class Body1 {
  String? value;
  String? type;
  String? purpose;
  String? created;
  String? modified;
  Creator? creator;

  Body1(
      {this.value,
      this.type,
      this.purpose,
      this.created,
      this.modified,
      this.creator});

  Body1.fromJson(Map<String, dynamic> json) {
    value = json['value'];
    type = json['type'];
    purpose = json['purpose'];
    created = json['created'];
    modified = json['modified'];
    creator =
        json['creator'] != null ? new Creator.fromJson(json['creator']) : null;
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['value'] = this.value;
    data['type'] = this.type;
    data['purpose'] = this.purpose;
    data['created'] = this.created;
    data['modified'] = this.modified;
    if (this.creator != null) {
      data['creator'] = this.creator!.toJson();
    }
    return data;
  }
}

class Creator1 {
  int? id;
  String? name;

  Creator1({this.id, this.name});

  Creator1.fromJson(Map<String, dynamic> json) {
    id = json['id'];
    name = json['name'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['id'] = this.id;
    data['name'] = this.name;
    return data;
  }
}

class Target1 {
  String? id;
  String? source;
  String? type;
  List<Selector>? selector;

  Target1({this.id, this.source, this.type, this.selector});

  Target1.fromJson(Map<String, dynamic> json) {
    id = json['id'];
    source = json['source'];
    type = json['type'];
    if (json['selector'] != null) {
      selector = <Selector>[];
      json['selector'].forEach((v) {
        selector!.add(new Selector.fromJson(v));
      });
    }
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['id'] = this.id;
    data['source'] = this.source;
    data['type'] = this.type;
    if (this.selector != null) {
      data['selector'] = this.selector!.map((v) => v.toJson()).toList();
    }
    return data;
  }
}

class Selector1 {
  String? exact;
  String? type;
  int? start;
  int? end;

  Selector1({this.exact, this.type, this.start, this.end});

  Selector1.fromJson(Map<String, dynamic> json) {
    exact = json['exact'];
    type = json['type'];
    start = json['start'];
    end = json['end'];
  }

  Map<String, dynamic> toJson() {
    final Map<String, dynamic> data = new Map<String, dynamic>();
    data['exact'] = this.exact;
    data['type'] = this.type;
    data['start'] = this.start;
    data['end'] = this.end;
    return data;
  }
}



