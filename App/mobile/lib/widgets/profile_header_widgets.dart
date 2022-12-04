import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:artopia/home_page.dart';
import 'package:artopia/routes.dart';
import 'package:artopia/profile.dart';
import 'package:artopia/profile_page.dart';
import 'package:artopia/templates.dart';
import 'package:artopia/register.dart';
import 'dart:core';
import 'package:avatar_glow/avatar_glow.dart';
import 'package:dotted_border/dotted_border.dart';
import 'package:http/http.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:artopia/utils/colorPalette.dart';
//import 'package:instagram_profile_page/data/data.dart';

Widget profileHeaderWidget(BuildContext context, Profile me) {
  final ColorPalette colorPalette = ColorPalette();

  return Container(
    width: double.infinity,
    decoration: BoxDecoration(
      color: colorPalette.frenchLilac,
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
                      glowColor: colorPalette.graniteGray,
                      endRadius: 90.0,
                      duration: Duration(milliseconds: 2000),
                      repeat: true,
                      showTwoGlows: true,
                      repeatPauseDuration: Duration(milliseconds: 100),
                      child: DottedBorder(
                        radius: Radius.circular(10),
                        color: colorPalette.graniteGray,
                        strokeWidth: 8,
                        borderType: BorderType.Circle,
                        dashPattern: [1, 12],
                        strokeCap: StrokeCap.butt,
                        child: Center(
                          child: SizedBox(
                            width: 130,
                            height: 130,
                            child: CircleAvatar(
                                
                              foregroundImage: Image.network(
                                      me.imageUrl)
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
                      Text(
                        me.username,
                        style: const TextStyle(
                          color: Colors.black87,
                          fontFamily: "OpenSans",
                          fontSize: 20.0,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ],
                  ),
                  SizedBox(height: 5),
                  Row(
                    children: [
                      Text(
                        me.name,
                      ),
                    ],
                  ),
                  SizedBox(height: 15),
                  Container(
                    width: 200,
                    child: Flexible(
                      child: Text(
                        me.bio,
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
                          Text(me.location),
                        ],
                      ),
                    ],
                  ),
                  SizedBox(height: 10),
                  Row(
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      Text("Followers "),
                      Text(me.followers.toString()),
                      SizedBox(width: 20),
                      Text(" Following "),
                      Text(me.following.toString()),
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
                padding: EdgeInsets.only(right: 30),
                child: ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    primary: colorPalette.blackShadows,
                    onPrimary: Colors.black,
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(10.0),
                    ),
                  ),
                  onPressed: () {
                    //Upload photos;
                  },
                  child: const Text('Upload'),
                ),
              ),
            ],
          ),
        ],
      ),
    ),
  );
}
