import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_app_mustafa/routes.dart';
import 'templates.dart';

class SignUpScreen extends StatefulWidget {

  @override
  State<SignUpScreen> createState() => _SignUpScreenState();
}

class _SignUpScreenState extends State<SignUpScreen> {
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
                          "Sign Up",
                          textAlign: TextAlign.left,
                          style: TextStyle(
                            color: Colors.white,
                            fontFamily: "OpenSans",
                            fontSize: 30.0,
                            fontWeight: FontWeight.bold,
                          )
                      ),
                      const SizedBox(height:30),
                      Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: <Widget>[
                          const Text(
                              "Username",
                              style: TextStyle(
                                color: Colors.white,
                                fontFamily: "OpenSans",
                                fontWeight: FontWeight.bold,
                              )
                          ),
                          const SizedBox(height: 10.0),
                          Container(
                            alignment: Alignment.centerLeft,
                            decoration:  BoxDecoration(
                              color: const Color.fromARGB(120, 175, 180, 255),
                              borderRadius: BorderRadius.circular(10),
                            ),
                            height: 60,
                            child: const TextField(
                              keyboardType: TextInputType.text,
                              style: TextStyle(
                                  color: Colors.white
                              ),
                              decoration: InputDecoration(
                                  border: InputBorder.none,
                                  contentPadding: EdgeInsets.only(top: 14),
                                  prefixIcon: Icon(Icons.email, color: Colors.white,),
                                  hintText: "Enter your username",
                                  hintStyle: TextStyle(
                                    color: Colors.white54,
                                    fontFamily: 'OpenSans',
                                  )
                              ),
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(height:10),
                      EmailInput(),
                      const SizedBox(height: 10),
                      PasswordInput(),
                      const SizedBox(height: 15),
                  Container(
                    alignment: Alignment.center,
                    padding: const EdgeInsets.symmetric(vertical: 10),
                    width: double.infinity,
                    child: ElevatedButton(
                        onPressed: ()=> print("Signed Up"),
                        style: ElevatedButton.styleFrom(
                          padding: const EdgeInsets.all(12.5),
                          minimumSize: const Size(400, 50),
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(15.0),
                          ),
                          backgroundColor: Colors.white,
                        ),
                        child: const Text(
                          "SIGN UP",
                          style: TextStyle(
                            color: Colors.black87,
                            fontFamily: "OpenSans",
                            fontSize: 20.0,
                            fontWeight: FontWeight.bold,
                          ),
                        )
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
