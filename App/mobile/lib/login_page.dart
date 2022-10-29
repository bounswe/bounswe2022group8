import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_app_mustafa/routes.dart';
import 'templates.dart';

class LoginScreen extends StatefulWidget {

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
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
                  gradient:SweepGradient(
                      center: FractionalOffset.topRight,
                      colors: <Color>[
                        Color.fromARGB(120, 0, 8, 193),
                        Color.fromARGB(120, 33, 70, 199),
                        Color.fromARGB(120, 175, 180, 255),
                        Color.fromARGB(120, 166, 225, 255),
                      ],
                    stops: <double>[0.25, 0.60, 0.750, 1],
                  )
                ),
              ),
              Container(
                alignment: Alignment.topCenter,
                height: double.infinity,
                padding: const EdgeInsets.symmetric(horizontal : 0, vertical: 40),
                child: Column(
                  children: const <Widget>[
                    LandingPageRoute(),
                  ],
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
                    children:  <Widget>[
                       const Text(
                          "Login",
                        textAlign: TextAlign.left,
                        style: TextStyle(
                          color: Colors.white,
                          fontFamily: "OpenSans",
                          fontSize: 30.0,
                          fontWeight: FontWeight.bold,
                        )
                      ),
                      const SizedBox(height:30),
                      EmailInput(),
                      const SizedBox(height: 10),
                      PasswordInput(),
                      const SizedBox(height: 20),
                      LoginButton(),
                      ForgotPassword(),
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
