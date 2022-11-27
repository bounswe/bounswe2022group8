import 'package:flutter/material.dart';
import 'package:artopia/login_page.dart';
import 'package:artopia/signup_page.dart';
import 'package:artopia/templates.dart';
import 'package:artopia/utils/colorPalette.dart';
import 'package:artopia/utils/textUtils.dart';

class LandingPageRoute extends StatelessWidget {
  const LandingPageRoute({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const BackToHomeButton();
  }
}

class LoginPageRoute extends StatelessWidget {
  LoginPageRoute({Key? key}) : super(key: key);
  final TextUtils textUtils = TextUtils();
  final ColorPalette colorPalette = ColorPalette();
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      style: ElevatedButton.styleFrom(
        padding: const EdgeInsets.all(12.5),
        minimumSize: const Size(400, 50),
        foregroundColor: colorPalette.frenchLilac,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(15.0),
        ),
        backgroundColor: colorPalette.frenchLilac,
      ),
      onPressed: () {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => LoginScreen()),
        );
      },
      child:
          textUtils.buildText("Login", 22.5, Colors.white70, FontWeight.w500),
    );
  }
}

class SignUpScreenRoute extends StatelessWidget {
  SignUpScreenRoute({Key? key}) : super(key: key);
  final TextUtils textUtils = TextUtils();
  final ColorPalette colorPalette = ColorPalette();
  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      style: ElevatedButton.styleFrom(
        padding: const EdgeInsets.all(12.5),
        minimumSize: const Size(400, 50),
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(15.0),
        ),
        backgroundColor: colorPalette.frenchLilac,
      ),
      onPressed: () {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => SignUpScreen()),
        );
      },
      child:
          textUtils.buildText("Sign Up", 22.5, Colors.white70, FontWeight.w500),
    );
  }
}

class HomePageRoute extends StatelessWidget {
  const HomePageRoute({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const ExitProfileButton();
  }
}

class ProfilePageRoute extends StatelessWidget {
  const ProfilePageRoute({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Container();
  }
}
