import 'package:flutter/material.dart';
import 'utils/colorPalette.dart';
import 'utils/textUtils.dart';
import 'dart:io';
import 'package:image_picker/image_picker.dart';
import 'package:flutter/services.dart';
import 'profile_page.dart';
import 'profile.dart';
import 'artitem.dart';
class UploadArtItem extends StatefulWidget {
  @override
  _UploadArtItem createState() => _UploadArtItem();
}

class _UploadArtItem extends State<UploadArtItem> {
  Future<Profile> myProfile = getMyProfile();
  final ColorPalette colorPalette = ColorPalette();
  final textUtils = TextUtils();
  final _formKey = GlobalKey<FormState>();
  XFile? image;
  final TextEditingController title = TextEditingController();
  final TextEditingController description = TextEditingController();
  final TextEditingController tags = TextEditingController();

  final ImagePicker picker = ImagePicker();

  Future getImage(ImageSource media) async {
    var img = await picker.pickImage(source: media);

    setState(() {
      image = img;
    });
  }

  //show popup dialog
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
                        Align(
                          alignment: Alignment.center,
                          child: textUtils.buildText(
                              "Upload an art item", 25, Colors.black, FontWeight.w500),
                        ),
                        const SizedBox(
                          height: 10,
                        ),
                        TextFormField(
                          controller: title,
                          decoration: InputDecoration(
                            icon: Icon(Icons.title_outlined,
                                color: colorPalette.darkPurple),
                            hintText: 'Please write the title of your art item',
                            labelText: 'Title',
                          ),
                          validator: (value) {
                            if (value?.isEmpty ?? true) {
                              return 'Please enter some text';
                            }
                            return null;
                          },
                        ),
                        const SizedBox(
                          height: 10,
                        ),
                        TextFormField(
                          controller: description,
                          decoration: InputDecoration(
                            icon: Icon(Icons.description_rounded,
                                color: colorPalette.darkPurple),
                            hintText:
                                'Please write the description of your art item',
                            labelText: 'Description',
                          ),
                          validator: (value) {
                            if (value?.isEmpty ?? true) {
                              return 'Please enter some text';
                            }
                            return null;
                          },
                        ),
                        const SizedBox(
                          height: 10,
                        ),
                        TextFormField(
                          controller: tags,
                          decoration: InputDecoration(
                            icon:
                                Icon(Icons.tag, color: colorPalette.darkPurple),
                            hintText: 'Please write tags for your art item',
                            labelText: 'Tags',
                          ),
                          validator: (value) {
                            if (value?.isEmpty ?? true) {
                              return 'Please enter some text';
                            }
                            return null;
                          },
                        ),
                        const SizedBox(
                          height: 10,
                        ),
                      ],
                    ),
                  ),
                ),
              ),
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
                },
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Icon(Icons.photo_size_select_actual_outlined),
                    const SizedBox(
                      width: 10,
                    ),
                    textUtils.buildText(
                        "Choose", 20, Colors.black, FontWeight.w500),
                  ],
                ),
              ),
            ),

            const SizedBox(
              height: 10,
            ),
            //if image not null show the image
            //if image null show text
            image != null
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
                : textUtils.buildText(
                "No art item is selected!", 20, Colors.black, FontWeight.w500),
            SizedBox(
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
                  if (_formKey.currentState!.validate() && (image == null)) {
                    // If the form is valid, display a Snackbar.
                    ScaffoldMessenger.of(context).showSnackBar(
                      const SnackBar(
                          content: Text('Please choose an art item.')),
                    );
                  }
                  if (_formKey.currentState!.validate() && (image != null)) {
                    // If the form is valid, display a Snackbar.
                    String tagString = tags.text;
                    String titleString = title.text;
                    String descriptionString = description.text ;
                    print(tagString + " " + titleString + " " + descriptionString);
                              uploadArtItem(titleString, descriptionString,tagString,image).then((value) {
                                if (value == "OK") {
                                  Route route = MaterialPageRoute(
                                      builder: (context) => const ProfilePage());
                                  Navigator.pushReplacement(context, route);
                                } else {
                              ScaffoldMessenger.of(context).showSnackBar(
                                    const SnackBar(
                                      content: Text('The art item is not uploaded.')),
                    );                                }
                              });
                    ScaffoldMessenger.of(context).showSnackBar(
                      const SnackBar(
                          content: Text('The art item is uploaded.')),
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
      ),

      ),
    );
  }
}
