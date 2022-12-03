import 'package:artopia/art_item_upload.dart';
import 'package:artopia/home_page.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:artopia/profile.dart';
import 'dart:core';
import 'package:avatar_glow/avatar_glow.dart';
import 'package:dotted_border/dotted_border.dart';
import 'package:artopia/utils/colorPalette.dart';
import 'package:artopia/utils/textUtils.dart';


Widget profileHeaderWidget(BuildContext context, Profile me) {
  final ColorPalette colorPalette = ColorPalette();
  final textUtils = TextUtils();
  void myAlert() {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
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
                  onPressed: () => {
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => UploadArtItem()
                        //myAlert(),
                        //Navigator.pop(context);
                        //getImage(ImageSource.gallery);
                      ),
                    ),
                  },
                  child: Row(
                    children: [
                      Icon(Icons.image),
                      SizedBox(
                        width: 10,
                      ),
                      textUtils.buildText(
                          "From Gallery", 13, Colors.black, FontWeight.w500),
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
                    //getImage(ImageSource.camera);
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
              ],
            ),
          ),
        );
      },
    );
  }
  return Container(
    width: double.infinity,
    decoration: BoxDecoration(
      color: colorPalette.graniteGray,
    ),
    child: Padding(
      padding: const EdgeInsets.only(left: 18.0, right: 18.0, bottom: 10),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              Padding(padding: const EdgeInsets.only(left: 5)),
              Column(
                children: [
                  SizedBox(
                    width: 120,
                    height: 120,
                    child: AvatarGlow(
                      glowColor: colorPalette.darkPurple,
                      endRadius: 90.0,
                      duration: Duration(milliseconds: 2000),
                      repeat: true,
                      showTwoGlows: true,
                      repeatPauseDuration: Duration(milliseconds: 100),
                      child: DottedBorder(
                        radius: Radius.circular(5),
                        color: colorPalette.darkPurple,
                        strokeWidth: 8,
                        borderType: BorderType.Circle,
                        dashPattern: [1, 12],
                        strokeCap: StrokeCap.butt,
                        child: Center(
                          child: SizedBox(
                            width: 130,
                            height: 130,
                            child: CircleAvatar(
                              foregroundImage: Image.asset(
                                  "assets/images/blank_profile.jpeg")
                                  .image,
                              radius: 10,
                            ),
                          ),
                        ),
                      ),
                    ),
                  ),
                ],
              ),
              Padding(padding: const EdgeInsets.only(left: 20)),
              Flex(
                direction: Axis.vertical,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  SizedBox(height: 20),
                  Row(
                    children: [
                      textUtils.buildText(
                          me.username, 18, Colors.white70, FontWeight.w500
                      ),
                    ],
                  ),
                  SizedBox(height: 5),
                  Row(
                    children: [
                      textUtils.buildText(
                          me.name, 13, Colors.white70, FontWeight.w500
                      ),
                    ],
                  ),
                  SizedBox(height: 15),
                  Container(
                    width: 200,
                    child: Flexible(
                      child: textUtils.buildText(
                          me.bio, 12, Colors.white70, FontWeight.w500
                      ),
                    ),
                  ),
                  SizedBox(height: 15),
                  Row(
                    children: [
                      Wrap(
                        crossAxisAlignment: WrapCrossAlignment.center,
                        children: [
                          Icon(Icons.location_on),
                          textUtils.buildText(
                              me.location, 12, Colors.white70, FontWeight.w500
                          ),
                        ],
                      ),
                    ],
                  ),
                  SizedBox(height: 10),
                  Row(
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      GestureDetector(
                        child: textUtils.buildText(
                            "Followers ", 12, Colors.black87, FontWeight.w500
                        ),
                        onTap: () => Navigator.push(
                          context,
                          MaterialPageRoute(builder: (context) => HomePage()),
                        ),
                      ),
                      textUtils.buildText(
                          me.followers.toString(), 12, Colors.black, FontWeight.w500
                      ),
                      SizedBox(width: 20),
                      GestureDetector(

                        child:
                        textUtils.buildText(
                            " Following ", 12, Colors.black87, FontWeight.w500
                        ),
                        onTap: () => Navigator.push(
                          context,
                          MaterialPageRoute(builder: (context) => HomePage()),
                        ),
                      ),
                      textUtils.buildText(
                          me.following.toString(), 13, Colors.black, FontWeight.w500
                      ),
                    ],
                  ),
                ],
              )
            ],
          ),
          Padding(padding: const EdgeInsets.only(top: 10)),
          Row(
            mainAxisAlignment: MainAxisAlignment.end,
            children: [
              Padding(
                padding: EdgeInsets.only(right: 25),
                child: ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: colorPalette.blackShadows,
                    foregroundColor: Colors.black,
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(10.0),
                    ),
                  ),
                  /*
                  onPressed: () {
                    myAlert();
                    //UploadArtItem();
                  },
                  */
                  onPressed: () => {
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => UploadArtItem()
                      ),
                    ),
                  },
                  child: textUtils.buildText(
                      "Add Art Item", 13, Colors.black, FontWeight.w500
                  ),
                ),
              ),
            ],
          ),
        ],
      ),
    ),
  );
}
