import 'package:artopia/templates.dart';
import 'package:flutter/material.dart';
import 'package:artopia/home_page.dart';
import 'package:artopia/landing_page.dart';
import 'package:artopia/login_page.dart';
import 'package:artopia/forgot_password.dart' ;
import 'package:artopia/confirm_password.dart' ;
// import 'package:artopia/profile_page.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      //home: ConfirmPasswordPage(),
      //home: ForgotPasswordPage(),
      home: LandingPage(),
      // home: ProfilePage(),
      // home: HomePage(),
    );
  }
}
