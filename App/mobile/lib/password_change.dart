import 'dart:math';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'variables.dart' ;
Future<String> sendOTP(email) async {
  final response = await http.post(
    Uri.parse(OTP_ENDPOINT),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, String>{
      'email': email,

    })
  ) ;
  print(response.statusCode) ;
  print(response.body) ;      
  
  Map<String, dynamic> body = jsonDecode(response.body);

  if (response.statusCode == 200) {

      return "OK" ;
  }
  else {
    return "Please check your email." ;
    
  }
}

Future<String> resetPassword(otp,email,password) async {
  final response = await http.put(
    Uri.parse(PASSWORD_RESET_ENDPOINT),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, String>{
      'email': email,
      'otp': otp,
      'new_password': password,

    })
  ) ;
  print(response.statusCode) ;
  print(response.body) ;      
  
  Map<String, dynamic> body = jsonDecode(response.body);

  if (response.statusCode == 200) {

      return "OK" ;
  }
  else {
    return "OTP or email did not match." ;
    
  }
}

