import 'dart:math';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'variables.dart' ;
Future<String> login(username,password) async {
  final response = await http.post(
    Uri.parse(LOGIN_ENDPOINT),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, String>{
      'credential': username,
      'password' : password,

    })
  ) ;
  print(response.statusCode) ;
  print(response.body) ;      
  
  Map<String, dynamic> body = jsonDecode(response.body);

  if (response.statusCode == 200) {
      token = body['token'] ;
      registered_username = username;
      return "OK" ;
  }
  else {
      if(username.length <1) return "Username cannot be empty" ;
      if(password.length <1) return "Password cannot be empty" ;

     if (body["credential"] != null)  return body["credential"][0] ;
    
    else if (body["password"] != null)   return body["password"][0] ;
    
    else   return "Please check your credentials for login." ;
    
  }
}

