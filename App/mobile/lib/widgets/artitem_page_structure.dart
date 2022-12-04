import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:artopia/utils/colorPalette.dart';
import 'package:artopia/utils/textUtils.dart';

class ArtItemPageStructue extends StatefulWidget {
  const ArtItemPageStructue({Key? key}) : super(key: key);

  @override
  State<ArtItemPageStructue> createState() => _ArtItemPageStructueState();
}

class _ArtItemPageStructueState extends State<ArtItemPageStructue> {
  final textUtils = TextUtils();
  final colorPalette = ColorPalette();

  @override
  Widget build(BuildContext context) {


    return Container(
      margin: const EdgeInsets.only(top: 5, bottom: 5),
      foregroundDecoration: BoxDecoration(
        border: Border.all(
          color: Colors.black,
          width: 4,
        ),
        borderRadius: BorderRadius.zero,
      ),
      decoration: const BoxDecoration(
        color: Colors.black,
        // color: colorPalette.palatinatePurple,
      ),
      alignment: Alignment.topCenter,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Row(
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [

              textUtils.buildText("TITLE GOES HERE", 32, colorPalette.blackShadows,
                  FontWeight.w600),
            ],
          ),
          const Padding(
            padding: EdgeInsets.only(left: 10, top: 10, right: 10),
          ),
          Image.asset(
            "assets/images/background.jpeg",
            height: MediaQuery.of(context).size.width,
            width: MediaQuery.of(context).size.width,
            alignment: Alignment.center,
            fit: BoxFit.cover,
          ),
          // const SizedBox(height: 10),
          const Padding(
            padding: EdgeInsets.only(bottom: 10),
          ),
          Row(
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Row(
                children: [
                  const SizedBox(
                    width: 15,
                  ),
                  const CircleAvatar(
                    radius: 25,
                    backgroundImage: AssetImage("assets/images/profile.jpeg"),
                  ),
                  const SizedBox(
                    width: 10,
                  ),
                  textUtils.buildText("selin", 20, colorPalette.blackShadows,
                      FontWeight.w600),
                ],
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.start,
                children: [
                  textUtils.buildText("458 likes", 13, colorPalette.blackShadows,
                      FontWeight.w600),
                  const SizedBox(
                    width: 15,
                  ),
                ],
              ),
            ],
          ),
          Padding(
            padding: const EdgeInsets.only(left: 10, top: 10, right: 10),
            child: Container(
              color: Colors.black,
              width: MediaQuery.of(context).size.width,
              height: 250,
              child: textUtils.buildText("Description goes here", 20, colorPalette.blackShadows,
                  FontWeight.w600),
            ),
          ),
        ],
      ),
    );
  }
}
