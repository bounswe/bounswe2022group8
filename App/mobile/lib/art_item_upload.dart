import 'package:flutter/material.dart';
import 'package:artopia/utils/colorPalette.dart';
import 'package:artopia/utils/textUtils.dart';
import 'dart:io';
import 'package:image_picker/image_picker.dart';
import 'package:flutter/services.dart';
import 'package:artopia/profile_page.dart';


class UploadArtItem extends StatefulWidget {
  @override
  _UploadArtItem createState() => _UploadArtItem();
}

class _UploadArtItem extends State<UploadArtItem> {
  final ColorPalette colorPalette = ColorPalette();
  final textUtils = TextUtils();

  XFile? image;

  final ImagePicker picker = ImagePicker();

  //we can upload image from camera or from gallery based on parameter
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
            shape:
            RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
            title: Text('Please choose media to select'),
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
                        Icon(Icons.image),
                        SizedBox(
                          width: 10,
                        ),
                        textUtils.buildText(
                            "From Gallery", 13, Colors.black, FontWeight.w500
                        ),
                      ],
                    ),

                  ),
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
                            "From Camera", 13, Colors.black, FontWeight.w500
                        ),
                      ],
                    ),

                  ),
                ],
              ),
            ),
          );
        });
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
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
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
                myAlert();
              },
              child: textUtils.buildText(
                  "Upload Art Item", 15, Colors.black, FontWeight.w500
              ),
            ),
            SizedBox(
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
                "No Image", 20, Colors.black, FontWeight.w500
            ),
          ],
        ),
      ),
    );
  }
}