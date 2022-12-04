import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:artopia/routes.dart';
import 'package:artopia/utils/textUtils.dart';
import 'package:artopia/utils/colorPalette.dart';

class LandingPage extends StatefulWidget {
  @override
  State<LandingPage> createState() => _LandingPageState();
}

class _LandingPageState extends State<LandingPage> {
  final TextUtils textUtils = TextUtils();
  final ColorPalette colorPalette = ColorPalette();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: AnnotatedRegion<SystemUiOverlayStyle>(
        value: SystemUiOverlayStyle.light,
        child: GestureDetector(
          onTap: () => FocusScope.of(context).unfocus(),
          child: Stack(
            children: <Widget>[
              Container(
                height: double.infinity,
                width: double.infinity,
                decoration: const BoxDecoration(
                  image: DecorationImage(
                      image: AssetImage('assets/images/background.jpeg'),
                      fit: BoxFit.cover),
                ),
              ),
              Container(
                alignment: Alignment.bottomCenter,
                height: double.infinity,
                child: SingleChildScrollView(
                  physics: const AlwaysScrollableScrollPhysics(),
                  padding: const EdgeInsets.symmetric(
                    horizontal: 40,
                    vertical: 60,
                  ),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: <Widget>[
                      textUtils.buildText("Welcome to Artopia", 32.5,
                          Colors.white, FontWeight.w400),
                      const SizedBox(height: 30),
                      LoginPageRoute(),
                      const SizedBox(height: 30),
                      SignUpScreenRoute(),
                      const SizedBox(height: 30),
                      ForgotPasswordScreenRoute(),
                    ],
                  ),
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
