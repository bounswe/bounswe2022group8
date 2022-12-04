import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'profile.dart';
import 'package:artopia/utils/colorPalette.dart';
import 'package:artopia/utils/textUtils.dart';
import 'package:artopia/profile_page.dart';
import 'package:artopia/change_password.dart';
import 'dart:io';
import 'package:image_picker/image_picker.dart';


class SettingsPage extends StatefulWidget {
  const SettingsPage({Key? key}) : super(key: key);
  @override
  State<SettingsPage> createState() => _SettingsPageState();
}

class _SettingsPageState extends State<SettingsPage> {
  Future<Profile> myProfile = getMyProfile();
  final ColorPalette colorPalette = ColorPalette();
  final textUtils = TextUtils();
  final _formKey = GlobalKey<FormState>();

  XFile? image;

  final ImagePicker picker = ImagePicker();

  Future getImage(ImageSource media) async {
    var img = await picker.pickImage(source: media);

    setState(() {
      image = img;
    });
  }

  void myAlert() {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
          title: Text('Please choose source to upload'),
          content: Container(
            height: MediaQuery.of(context).size.height / 6,
            child: Column(
              children: [
                ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: colorPalette.blackShadows,
                    foregroundColor: Colors.black,
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(10.0),
                    ),
                  ),
                  onPressed: () {
                    Navigator.pop(context);
                    getImage(ImageSource.gallery);
                  },
                  child: Row(
                    children: [
                      Icon(Icons.photo_library_outlined),
                      SizedBox(
                        width: 10,
                      ),
                      textUtils.buildText(
                          "From Gallery", 13, Colors.black, FontWeight.w500),
                    ],
                  ),
                ),
                /*
                ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: colorPalette.blackShadows,
                    foregroundColor: Colors.black,
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(10.0),
                    ),
                  ),
                  onPressed: () {
                    Navigator.pop(context);
                    getImage(ImageSource.camera);
                  },
                  child: Row(
                    children: [
                      Icon(Icons.camera),
                      SizedBox(
                        width: 10,
                      ),
                      textUtils.buildText(
                          "From Camera", 13, Colors.black, FontWeight.w500),
                    ],
                  ),
                ),
                */
              ],
            ),
          ),
        );
      },
    );
  }

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
        child: Container(
      //alignment: Alignment.bottomCenter,
      height: double.infinity,
      child: SingleChildScrollView(
        physics: const AlwaysScrollableScrollPhysics(),
        /*
        padding: const EdgeInsets.symmetric(
          horizontal: 40,
          vertical: 60,
        ),
        */
        child:
        Column(
          children: [
            const SizedBox(
              height: 10,
            ),
            SizedBox(
              child: Form(
                key: _formKey,
                child: Theme(
                  data: ThemeData(
                    textSelectionTheme: TextSelectionThemeData(
                      cursorColor: colorPalette.blackShadows,
                      selectionColor: colorPalette.blackShadows,
                    ),
                    inputDecorationTheme: InputDecorationTheme(
                      contentPadding: const EdgeInsets.symmetric(
                          vertical: 10.0, horizontal: 10.0),
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
                        fontSize: 14,
                        color: colorPalette.darkPurple,
                      ),
                      errorStyle: TextStyle(
                        color: Colors.red[900],
                      ),
                      hintStyle: TextStyle(
                        fontSize: 14,
                        color: colorPalette.darkPurple,
                      ),
                      labelStyle: TextStyle(
                        fontSize: 12,
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
                        const SizedBox(
                          height: 10,
                        ),
                        Align(
                          alignment: Alignment.center,
                          child: textUtils.buildText("Edit your profile", 25,
                              Colors.black, FontWeight.w500),
                        ),
                        const SizedBox(
                          height: 10,
                        ),
                        Align(
                          alignment: Alignment.centerLeft,
                          child: Padding(
                            padding: EdgeInsets.only(left: 40),
                            child: ElevatedButton(
                              style: ElevatedButton.styleFrom(
                                backgroundColor: colorPalette.blackShadows,
                                foregroundColor: Colors.black,
                                shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(10.0),
                                ),
                              ),
                              onPressed: () => {
                                Navigator.push(
                                  context,
                                  MaterialPageRoute(builder: (context) => ChangePassword(name: "Password")
                                  ),
                                ),
                              },
                              child: textUtils.buildText(
                                  "Change Your Password", 13, Colors.black, FontWeight.w500
                              ),
                            ),
                          ),
                        ),
                        const SizedBox(
                          height: 10,
                        ),

                        SizedBox(
                          height: 35,
                          child: TextFormField(
                            decoration: InputDecoration(
                              icon: Icon(Icons.person,
                                  color: colorPalette.darkPurple),
                              hintText: 'Edit your name',
                              labelText: 'Name',
                            ),
                            validator: (value1) {
                              if (value1?.isEmpty ?? true) {
                                print("No edit");
                              }
                              return null;
                            },
                          ),
                        ),
                        const SizedBox(
                          height: 10,
                        ),
                        SizedBox(
                          height: 35,
                          child: TextFormField(
                            decoration: InputDecoration(
                              icon: Icon(Icons.person,
                                  color: colorPalette.darkPurple),
                              hintText: 'Edit your surname',
                              labelText: 'Surname',
                            ),
                            validator: (value2) {
                              if (value2?.isEmpty ?? true) {
                                print("No edit");
                              }
                              return null;
                            },
                          ),
                        ),
                        const SizedBox(
                          height: 10,
                        ),
                        SizedBox(
                          height: 35,
                          child: TextFormField(
                            decoration: InputDecoration(
                              icon: Icon(Icons.description_rounded,
                                  color: colorPalette.darkPurple),
                              hintText: 'Edit your bio',
                              labelText: 'Bio',
                            ),
                            validator: (value3) {
                              if (value3?.isEmpty ?? true) {
                                print("No edit");
                              }
                              return null;
                            },
                          ),
                        ),
                        const SizedBox(
                          height: 10,
                        ),
                        SizedBox(
                          height: 35,
                          child: TextFormField(
                            decoration: InputDecoration(
                              icon: Icon(Icons.person_pin_circle_outlined,
                                  color: colorPalette.darkPurple),
                              hintText: 'Edit your location',
                              labelText: 'Location',
                            ),
                            validator: (value4) {
                              if (value4?.isEmpty ?? true) {
                                print("No edit");
                              }
                              return null;
                            },
                          ),
                        ),
                      ],
                    ),
                  ),
                ),
              ),
            ),
            const SizedBox(
              height: 20,
            ),
            SizedBox(
              child: image != null
                  ? Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 20),
                      child: ClipRRect(
                        borderRadius: BorderRadius.circular(8),
                        child: Image.file(
                          //to show image, you type like this.
                          File(image!.path),
                          fit: BoxFit.cover,
                          width: MediaQuery.of(context).size.width,
                          height: 300,
                        ),
                      ),
                    )
                  : textUtils.buildText("No photo is selected! ", 20,
                      Colors.black, FontWeight.w500),
            ),
            const SizedBox(
              height: 10,
            ),
            SizedBox(
              width: MediaQuery.of(context).size.height / 3.5,
              child: ElevatedButton(
                style: ElevatedButton.styleFrom(
                  backgroundColor: colorPalette.blackShadows,
                  foregroundColor: Colors.black,
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10.0),
                  ),
                ),
                onPressed: () {
                  myAlert();
                  //Navigator.pop(context);
                  //getImage(ImageSource.gallery);
                },
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Icon(Icons.photo_size_select_actual_outlined, size: 18),
                    SizedBox(
                      width: 10,
                    ),
                    textUtils.buildText("Choose a profile photo", 15,
                        Colors.black, FontWeight.w500),
                  ],
                ),
              ),
            ),
            const SizedBox(
              height: 10,
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
                  if (!(_formKey.currentState!.validate()) && (image == null)) {
                    // If the form is valid, display a Snackbar.
                    ScaffoldMessenger.of(context).showSnackBar(
                      const SnackBar(
                          content: Text('Please choose a profile photo.')),
                    );
                  }
                },
                child: textUtils.buildText(
                    "Save", 20, Colors.black, FontWeight.w500),
              ),
            ),
          ],
        ),
      ),
        ),
      ),
    );
  }
}
