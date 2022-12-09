import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'profile.dart';
import 'utils/colorPalette.dart';
import 'utils/textUtils.dart';
import 'profile_page.dart';
import 'settings_page.dart';
import 'dart:async';


class ChangePassword extends StatefulWidget {
  ChangePassword({Key? key, required this.name}) : super(key: key);
  final String name;
  @override
  State<ChangePassword> createState() => _ChangePasswordState();
}

class _ChangePasswordState extends State<ChangePassword> {
  Future<Profile> myProfile = getMyProfile();
  final ColorPalette colorPalette = ColorPalette();
  final textUtils = TextUtils();
  final GlobalKey<FormState> _form = GlobalKey<FormState>();
  final TextEditingController _pass = TextEditingController();
  final TextEditingController _confirmPass = TextEditingController();
  var confirmPass;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: PreferredSize(
        preferredSize: Size.fromHeight(40),
        child: Container(
          decoration: BoxDecoration(
            border: Border(
              bottom: BorderSide(
                width: 1,
                color: colorPalette.darkPurple,
              ),
            ),
          ),
          child: AppBar(
            centerTitle: true,
            automaticallyImplyLeading: false,
            backgroundColor: colorPalette.darkPurple,
            leading: IconButton(
              icon: Icon(Icons.arrow_back),
              color: colorPalette.russianGreen,
              tooltip: 'Back to profile page',
              onPressed: () => {
                Navigator.pop(
                  context,
                  MaterialPageRoute(builder: (context) => ProfilePage()),
                )
              },
            ),
            title: textUtils.buildText(
                "artopia", 25, Colors.white70, FontWeight.w500),
          ),
        ),
      ),
      body: Center(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            const SizedBox(
              height: 10,
            ),
            Align(
              alignment: Alignment.center,
              child: textUtils.buildText(
                  "Change your password", 25, Colors.black, FontWeight.w500),
            ),
            const SizedBox(
              height: 20,
            ),
            SizedBox(
              child: Form(
                key: _form,
                child: Theme(
                  data: ThemeData(
                    textSelectionTheme: TextSelectionThemeData(
                      cursorColor: colorPalette.blackShadows,
                      selectionColor: colorPalette.blackShadows,
                    ),
                    inputDecorationTheme: InputDecorationTheme(
                      errorBorder: OutlineInputBorder(
                        borderSide: BorderSide(color: colorPalette.darkPurple),
                        borderRadius: BorderRadius.circular(10),
                      ),
                      enabledBorder: OutlineInputBorder(
                        borderSide: BorderSide(color: colorPalette.darkPurple),
                        borderRadius: BorderRadius.circular(10),
                      ),
                      focusedBorder: OutlineInputBorder(
                        borderSide: BorderSide(color: colorPalette.darkPurple),
                        borderRadius: BorderRadius.circular(10),
                      ),
                      border: OutlineInputBorder(
                        borderSide: BorderSide(color: colorPalette.darkPurple),
                        borderRadius: BorderRadius.circular(10),
                      ),
                      helperStyle: TextStyle(
                        color: colorPalette.darkPurple,
                      ),
                      floatingLabelStyle: TextStyle(
                        color: colorPalette.darkPurple,
                      ),
                      errorStyle: TextStyle(
                        color: Colors.red[900],
                      ),
                      hintStyle: TextStyle(
                        color: colorPalette.darkPurple,
                      ),
                      labelStyle: TextStyle(
                        color: colorPalette.darkPurple,
                      ),
                      prefixStyle: TextStyle(
                        color: colorPalette.darkPurple,
                      ),
                      suffixStyle: TextStyle(
                        color: colorPalette.darkPurple,
                      ),
                      counterStyle: TextStyle(
                        color: colorPalette.darkPurple,
                      ),
                    ),
                  ),
                  child: Container(
                    margin: EdgeInsets.only(left: 5.0, right: 10.0),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: <Widget>[
                        TextFormField(
                          autocorrect: false,
                          controller: _pass,
                          obscureText: true,
                          keyboardType: TextInputType.visiblePassword,
                          decoration: InputDecoration(
                            icon: Icon(Icons.lock_sharp,
                                color: colorPalette.darkPurple),
                            hintText: 'Please enter your new password',
                            labelText: 'New Password',
                          ),
                          validator: (value) {
                            confirmPass = value;
                            if (value?.isEmpty ?? true) {
                              return "Please Enter New Password";
                            } else if (value!.length < 10) {
                              return "Password must be at least 10 characters long";
                            } else {
                              return null;
                            }
                          },
                        ),
                        const SizedBox(
                          height: 20,
                        ),
                        TextFormField(
                          autocorrect: false,
                          controller: _confirmPass,
                          obscureText: true,
                          keyboardType: TextInputType.visiblePassword,
                          decoration: InputDecoration(
                            icon: Icon(Icons.lock_reset_sharp,
                                color: colorPalette.darkPurple),
                            hintText:
                            'Please re-enter your new password',
                            labelText: 'New Password (again)',
                          ),
                          validator: (value) {
                            if (value?.isEmpty ?? true) {
                              return "Please Re-Enter New Password";
                            } else if (value!.length < 10) {
                              return "Password must be at least 10 characters long";
                            } else if (value != confirmPass) {
                              return "Password must be same as above";
                            } else {
                              return null;
                            }
                          },
                        ),
                        const SizedBox(
                          height: 20,
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ),
            SizedBox(
              child: ElevatedButton(
                style: ElevatedButton.styleFrom(
                  backgroundColor: colorPalette.blackShadows,
                  foregroundColor: Colors.black,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10.0),
                  ),
                ),
                onPressed: () {
                  // It returns true if the form is valid, otherwise returns false
                  if (_form.currentState!.validate()) {
                    // If the form is valid, display a Snackbar.
                    ScaffoldMessenger.of(context).showSnackBar(
                      const SnackBar(
                        duration: Duration(milliseconds: 800),
                          content: Text('Your password has been changed!')),
                    );
                    //Return to settings page
                    Timer(
                      const Duration(milliseconds: 1000),
                          () {
                            Navigator.pop(
                              context,
                              MaterialPageRoute(builder: (context) => SettingsPage()),
                            );
                      },
                    );

                  }
                },
                child: textUtils.buildText(
                    "Submit", 20, Colors.black, FontWeight.w500),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
