import 'package:artopia/password_change.dart';
import 'package:artopia/templates.dart';
import 'package:artopia/variables.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:artopia/home_page.dart';
import 'package:artopia/routes.dart';
import 'package:artopia/utils/textUtils.dart';
import 'package:artopia/utils/colorPalette.dart';
import 'package:artopia/password_change.dart';
import 'package:artopia/confirm_password.dart';

//import 'templates.dart';
//import 'login.dart';

class ForgotPasswordPage extends StatefulWidget {
  @override
  State<ForgotPasswordPage> createState() => _ForgotPasswordState();
}

class _ForgotPasswordState extends State<ForgotPasswordPage> {
  String _error = "Hello There!";
  final TextUtils textUtils = TextUtils();
  final ColorPalette colorPalette = ColorPalette();
  final EmailInputObject = EmailInput();
  Future<String>? _loginResponseMessage;

  void _setErrorMessage({String error = ""}) {
    setState(() {
      _error = error;
    });
  }

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
                alignment: Alignment.topCenter,
                height: double.infinity,
                padding:
                    const EdgeInsets.symmetric(horizontal: 0, vertical: 40),
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
                    children: <Widget>[
                      textUtils.buildText("Forgot your password?", 30,
                          Colors.white, FontWeight.bold),
                      const SizedBox(height: 5),
                      textUtils.buildText(_error, 16,
                          Colors.white, FontWeight.bold),
                      EmailInputObject,
                      const SizedBox(height: 10),
                      Container(
                        alignment: Alignment.center,
                        padding: const EdgeInsets.symmetric(vertical: 10),
                        width: double.infinity,
                        child: ElevatedButton(
                            onPressed: () {
                        String email =
                                  EmailInputObject.emailController.text;
                              sendOTP(email).then((value) {
                                if (value == "OK") {
                                  change_email = email ;
                                  Route route = MaterialPageRoute(
                                      builder: (context) =>  ConfirmPasswordPage());
                                  Navigator.pushReplacement(context, route);
                                } else {
                                  _setErrorMessage(error: value);
                                }

                             
                              ;
                            },); },
                            style: ElevatedButton.styleFrom(
                              padding: const EdgeInsets.all(12.5),
                              minimumSize: const Size(400, 50),
                              shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(15.0),
                              ),
                              backgroundColor: colorPalette.russianGreen,
                            ),
                            child: textUtils.buildText("Send me the security code", 20,
                                Colors.white, FontWeight.bold),
                        ),
                      ),
                      // ForgotPassword(),
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
