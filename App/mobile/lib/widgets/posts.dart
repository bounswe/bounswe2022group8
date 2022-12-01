import 'package:flutter/material.dart';
import 'package:artopia/utils/colorPalette.dart';
import 'package:artopia/utils/textUtils.dart';
import 'package:artopia/artitem.dart';

class PostsList extends StatefulWidget {
  //baglama isi icin bu satiri da commentli birakiyorum
  // final ArtItem artItem;
  final owner = "Author";
  PostsList({Key?key}) : super(key: key);
  //baglama isini kolaylastirmak icin bu satiri burada birakmak mantikli.
  // PostsList({Key?key, required this.artItem}) : super(key: key);
  @override
  State<PostsList> createState() => _PostsListState();
}

class _PostsListState extends State<PostsList> {
  final textUtils = TextUtils();
  final colorPalette = ColorPalette();
  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(top: 5,bottom: 5),
      foregroundDecoration: BoxDecoration(
        border: Border.all(
          color: colorPalette.frenchLilac,
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
          Padding(
            padding: const EdgeInsets.only(left: 10, top: 10, right: 10),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children:  [
                Row(
                  children: [
                    const CircleAvatar(
                      radius: 16,
                      backgroundImage: AssetImage("assets/images/profile.jpeg"),
                    ),
                    const SizedBox(
                      width: 10,
                    ),
                    textUtils.buildText("selin", 16, colorPalette.blackShadows, FontWeight.w600),
                  ],
                ),
                Row(
                  children: [
                    textUtils.buildText("Title", 16, colorPalette.blackShadows, FontWeight.w600),
                  ],
                )
              ],
            ),
          ),
          const SizedBox(height: 10),
          Image.asset(
              "assets/images/background.jpeg",
              height:MediaQuery.of(context).size.width,
              width: MediaQuery.of(context).size.width,
              alignment: Alignment.center,
              fit: BoxFit.cover,
          ),
          const SizedBox(height: 10),
          Padding(
            padding: const EdgeInsets.only(bottom: 10),
            child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: [
                    Icon(
                      Icons.heart_broken_rounded,
                      color: colorPalette.blackShadows,
                      size: 30,
                    ),
                    Icon(
                          Icons.message,
                          color: colorPalette.blackShadows,
                          size: 30),
                    Icon(
                      Icons.attach_money,
                      color: colorPalette.blackShadows,
                      size: 30,
                    )
              ],
            ),
          ),
        ],
      ),
    );
  }
}
