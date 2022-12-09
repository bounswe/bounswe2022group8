import 'package:artopia/artitem.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import '../utils/colorPalette.dart';
import '../utils/textUtils.dart';

class ArtItemPageStructue extends StatefulWidget {
  final ArtItem artitem ;
  const ArtItemPageStructue({Key? key , required  this.artitem}) : super(key: key);

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

              textUtils.buildText(widget.artitem.title, 32, colorPalette.blackShadows,
                  FontWeight.w600),
            ],
          ),
          const Padding(
            padding: EdgeInsets.only(left: 10, top: 10, right: 10),
          ),
          Image.network(
            widget.artitem.artitem_path,
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
                   CircleAvatar(
                    radius: 25,
                    backgroundImage: Image.network( widget.artitem.profile_path).image,
                  ),
                  const SizedBox(
                    width: 10,
                  ),
                  textUtils.buildText(widget.artitem.username, 20, colorPalette.blackShadows,
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
              child: textUtils.buildText(widget.artitem.description, 20, colorPalette.blackShadows,
                  FontWeight.w600),
            ),
          ),
        ],
      ),
    );
  }
}
