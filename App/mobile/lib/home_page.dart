import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_app_mustafa/routes.dart';

class HomePage extends StatefulWidget {

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
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
                    children:  const <Widget>[
                      Text(
                          "Welcome to MyApp",
                          textAlign: TextAlign.left,
                          style: TextStyle(
                            color: Colors.white,
                            fontFamily: "OpenSans",
                            fontSize: 30.0,
                            fontWeight: FontWeight.bold,
                          )
                      ),
                      SizedBox(height: 30),
                      LoginScreenRoute(),
                      SizedBox(height: 30),
                      SignUpScreenRoute(),
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
