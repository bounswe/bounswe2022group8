import 'package:flutter/material.dart';
import 'package:flutter_app_mustafa/login_page.dart';
import 'package:flutter_app_mustafa/signup_page.dart';
import 'package:flutter_app_mustafa/templates.dart';

class LoginPageRoute extends StatelessWidget {
  const LoginPageRoute({Key? key}) : super(key: key);

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
        child: const Text(
        "LOGIN",
        style: TextStyle(
        color: Colors.black87,
        fontFamily: "OpenSans",
        fontSize: 20.0,
        fontWeight: FontWeight.bold,
          ),
        ),
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
  const SignUpScreenRoute({Key? key}) : super(key: key);

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
      child: const Text(
        "SIGN UP",
        style: TextStyle(
          color: Colors.black87,
          fontFamily: "OpenSans",
          fontSize: 20.0,
          fontWeight: FontWeight.bold,
        ),
      ),
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


