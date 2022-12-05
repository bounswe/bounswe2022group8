import '../artitem_page.dart';
import 'package:flutter/material.dart';
import '../utils/colorPalette.dart';
import '../utils/textUtils.dart';
import '../comment_page.dart';

import 'artitem_page_structure.dart';

//  baglama isi yaparken kullanilacak.
// import 'artitem.dart';

class Post extends StatefulWidget {

  //baglama isi icin bu satiri da commentli birakiyorum
  // final ArtItem artItem;
  final owner = "Author";
  const Post({Key? key}) : super(key: key);

  //baglama isini kolaylastirmak icin bu satiri burada birakmak mantikli.
  // PostsList({Key?key, required this.artItem}) : super(key: key);

  @override
  State<Post> createState() => _PostState();


  createArtItemPage() => ArtItemPageStructue();
}

class _PostState extends State<Post> {
  final textUtils = TextUtils();
  final colorPalette = ColorPalette();
  @override
  Widget build(BuildContext context) {
    IconButton likeButton = IconButton(
      icon: Icon(Icons.favorite, color: colorPalette.blackShadows, size: 30),
      tooltip: 'Like',
      splashColor: Colors.white,
      onPressed: () => {likeButtonPressed()},
    );

    IconButton commentButton = IconButton(
      icon: Icon(Icons.comment_outlined,
          color: colorPalette.blackShadows, size: 30),
      tooltip: 'Comment',
      onPressed: () => {commentButtonPressed()},
    );

    IconButton purchaseButton = IconButton(
      icon: Icon(
        Icons.attach_money,
        color: colorPalette.blackShadows,
        size: 30,
      ),
      tooltip: 'pURCHASE',
      onPressed: () => {purchaseButtonPressed()},
    );

    return Container(
      margin: const EdgeInsets.only(top: 5, bottom: 5),
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
              children: [
                Row(
                  children: [
                    const CircleAvatar(
                      radius: 16,
                      backgroundImage: AssetImage("assets/images/profile.jpeg"),
                    ),
                    const SizedBox(
                      width: 10,
                    ),
                    textUtils.buildText("selin", 16, colorPalette.blackShadows,
                        FontWeight.w600),
                  ],
                ),
                Row(
                  children: [
                    textUtils.buildText("Title", 16, colorPalette.blackShadows,
                        FontWeight.w600),
                  ],
                )
              ],
            ),
          ),
          const SizedBox(height: 10),
          Image.asset(
            "assets/images/background.jpeg",
            height: MediaQuery.of(context).size.width,
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
                likeButton,
                commentButton,
                purchaseButton
              ],
            ),
          ),
        ],
      ),
    );
  }

  likeButtonPressed() {
    print("like button pressed");
  }

  commentButtonPressed() {
    print("comment button pressed");
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => const CommentPage()),
    );
  }

  purchaseButtonPressed() {
    print("purchase button pressed");
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => const ArtItemPage()),
    );
  }
}
