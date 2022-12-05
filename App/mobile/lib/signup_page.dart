import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:artopia/home_page.dart';
import 'package:artopia/login_page.dart';
import 'package:artopia/routes.dart';
import 'package:artopia/utils/textUtils.dart';
import 'package:artopia/utils/colorPalette.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:url_launcher/url_launcher.dart';
import 'templates.dart';
import 'register.dart';

class SignUpScreen extends StatefulWidget {
  @override
  State<SignUpScreen> createState() => _SignUpScreenState();
}

class _SignUpScreenState extends State<SignUpScreen> {
  String _error = "Welcome to Artopia!";
  bool value = false;
  final TextUtils textUtils = TextUtils();
  final ColorPalette colorPalette = ColorPalette();
  final usernameController = TextEditingController();
  final EmailInputObject = EmailInput();
  final PasswordInputObject = PasswordInput(name: "Password");
  final ConfirmPasswordInputObject = PasswordInput(name: "Confirm Password");
  Future<String>? _registerResponseMessage;

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
                      textUtils.buildText("Sign Up", 30,
                          Colors.white, FontWeight.bold),
                      const SizedBox(height: 5),
                      textUtils.buildText(_error, 14,
                          Colors.white, FontWeight.bold),
                      const SizedBox(height: 30),
                      Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: <Widget>[
                          textUtils.buildText("Username", 14,
                              Colors.white, FontWeight.bold),
                          const SizedBox(height: 10.0),
                          Container(
                            alignment: Alignment.centerLeft,
                            decoration: BoxDecoration(
                              color: const Color.fromARGB(120, 175, 180, 255),
                              borderRadius: BorderRadius.circular(10),
                            ),
                            height: 60,
                            child: TextField(
                              controller: usernameController,
                              keyboardType: TextInputType.text,
                              style: const TextStyle(color: Colors.white),
                              decoration: InputDecoration(
                                  border: InputBorder.none,
                                  contentPadding: const EdgeInsets.only(top: 14),
                                  prefixIcon: const Icon(
                                    Icons.email,
                                    color: Colors.white,
                                  ),
                                  hintText: "Enter your username",
                                  hintStyle: GoogleFonts.inter(
                                    fontSize: 14,
                                    color: Colors.white54,
                                  ),
                              ),
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height: 10),
                      EmailInputObject,
                      const SizedBox(height: 10),
                      PasswordInputObject,
                      const SizedBox(height: 10),
                      ConfirmPasswordInputObject,
                      Row(
                        mainAxisAlignment: MainAxisAlignment.start,
                        children: <Widget>[
                          Checkbox(value: value,
                              side: const BorderSide(color: Colors.white),
                              onChanged:
                                  (bool? value) {
                                setState(() {
                                  this.value = value!;
                                });
                              }),
                          SizedBox(
                            width: 260,
                            child:
                            InkWell(
                              onTap: () => launchUrl(Uri.parse('https://www.lipsum.com')),
                              child: Text(
                                'I agree to the Terms and Conditions',
                                style: GoogleFonts.inter(
                                  fontSize: 14,
                                  color: Colors.white,
                                  decoration: TextDecoration.underline
                                ),
                              ),
                            )
                          ),
                        ], //<Widget>[]
                      ),
                      Container(
                        alignment: Alignment.center,
                        padding: const EdgeInsets.symmetric(vertical: 10),
                        width: double.infinity,
                        child: ElevatedButton(
                            onPressed: () {
                                if (value == false){
                                  _setErrorMessage(error: "Please accept the Terms and Conditions.");
                                  }
                                else {
                              String username = usernameController.text;
                              String email =
                                  EmailInputObject.emailController.text;
                              String password =
                                  PasswordInputObject.passwordController.text;
                              String confirmPassword =
                                  ConfirmPasswordInputObject
                                      .passwordController.text;
                              print(username +
                                  email +
                                  password +
                                  confirmPassword);
                              register(username, email, password,
                                      confirmPassword)
                                  .then((value) {
                                if (value == "OK") {
                       
                                  Route route = MaterialPageRoute(
                                      builder: (context) => LoginScreen());
                                  Navigator.pushReplacement(context, route);
                                  
                                } else {
                                  _setErrorMessage(error: value);
                                }
                                print(value);
                              });
                            }
                            },
                            style: ElevatedButton.styleFrom(
                              padding: const EdgeInsets.all(12.5),
                              minimumSize: const Size(400, 50),
                              shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(15.0),
                              ),
                              backgroundColor: colorPalette.frenchLilac,
                            ),
                            child: textUtils.buildText("Sign Up", 20, Colors.white, FontWeight.bold)
                        ),
                      ),
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
