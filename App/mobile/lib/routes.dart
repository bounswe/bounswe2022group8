import 'package:flutter/material.dart';
import 'package:flutter_app_mustafa/login_page.dart';
import 'package:flutter_app_mustafa/signup_page.dart';
import 'package:flutter_app_mustafa/templates.dart';
import 'package:flutter_app_mustafa/utils/textUtils.dart';

class LoginPageRoute extends StatelessWidget {
  LoginPageRoute({Key? key}) : super(key: key);
  final TextUtils textUtils = TextUtils();
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
        style: ElevatedButton.styleFrom(
        padding: const EdgeInsets.all(12.5),
        minimumSize: const Size(400, 50),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(15.0),
        ),
        backgroundColor: Colors.white,
      ),
      onPressed: () {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => LoginScreen()),
        );
      },
        child:
        textUtils.buildText("Login", 20.0, Colors.black, FontWeight.w500),
    );
  }
}

class LandingPageRoute extends StatelessWidget {
  const LandingPageRoute({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return BackToHomeButton();
  }
}

class SignUpScreenRoute extends StatelessWidget {
  SignUpScreenRoute({Key? key}) : super(key: key);
  final TextUtils textUtils = TextUtils();

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      style: ElevatedButton.styleFrom(
        padding: const EdgeInsets.all(12.5),
        minimumSize: const Size(400, 50),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(15.0),
        ),
        backgroundColor: Colors.white,
      ),
      onPressed: () {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => SignUpScreen()),
        );
      },
      child:
      textUtils.buildText("Sign Up", 20.0, Colors.black, FontWeight.w500),
    );
  }
}

class HomePageRoute extends StatelessWidget {
  const HomePageRoute({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Container();
  }
}


