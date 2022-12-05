import 'dart:math';

import 'package:http/http.dart' as http;
import 'dart:convert';
import 'variables.dart' ;
Future<String> register(username,email,password,confirmPassword) async {
  final response = await http.post(
    Uri.parse(REGISTER_ENDPOINT),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, String>{
      'email': email,
      'password' : password,
      'password_confirm' : confirmPassword,
      'username' : username,
    })
  ) ;
  print(response.statusCode) ;
  print(response.body) ;      
  
  Map<String, dynamic> body = jsonDecode(response.body);

  if (response.statusCode == 201) {
      token = body['token'] ;
      registered_username = username ;
      registered_password = password ;
      return "OK" ;
  }
  else {
      if(username.length <1) return "Username cannot be empty" ;
      if(email.length <1) return "Email cannot be empty" ;
      if(password.length <1) return "Password cannot be empty" ;
      if(confirmPassword.length <1) return "Confirm Passwordr cannot be empty" ;

      
    if(body["username"] != null) {

      return body["username"][0] ;
    }
    else if (body["email"] != null) {
      return body["email"][0] ;
    }
    else if (body["password"] != null) {
      return body["password"][0] ;
    }
    else {
      return "Please check your credentials for signup." ;
    }
  }
return "NOT OK" ;
}

