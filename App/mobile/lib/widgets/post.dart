import 'package:artopia/artitem.dart';
import 'package:artopia/artitem_page.dart';
import 'package:flutter/material.dart';
import '../utils/colorPalette.dart';
import '../utils/textUtils.dart';
import '../comment_page.dart';
import 'artitem_page_structure.dart';

class Post extends StatefulWidget {

  final ArtItem artitem ;
  final owner = "Author";


  const Post({Key? key,required this.artitem}) : super(key: key);

  @override
  State<Post> createState() => _PostState();


  createArtItemPage() => ArtItemPageStructue(artitem: artitem,);
}

class _PostState extends State<Post> {
  final textUtils = TextUtils();
  final colorPalette = ColorPalette();
  bool liked = false;

  void changeLikeState(){
    setState(() {
      liked = !liked;
    });
  }

  @override
  Widget build(BuildContext context) {
    IconButton likeButton = IconButton(
      icon: liked ?  Icon(Icons.favorite, color: colorPalette.blackShadows, size: 30) : Icon(Icons.favorite_border_outlined, color: colorPalette.blackShadows, size: 30),
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
        Icons.description_outlined,
        color: colorPalette.blackShadows,
        size: 30,
      ),
      tooltip: 'Details',
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
                     CircleAvatar(
                      radius: 16,
                      backgroundImage: Image.network(widget.artitem.profile_path).image,
                    ),
                    const SizedBox(
                      width: 10,
                    ),
                    textUtils.buildText(widget.artitem.username, 16, colorPalette.blackShadows,
                        FontWeight.w600),
                  ],
                ),
                Row(
                  children: [
                    textUtils.buildText(widget.artitem.title, 16, colorPalette.blackShadows,
                        FontWeight.w600),
                  ],
                )
              ],
            ),
          ),
           SizedBox(height: 10),
          Image.network(
            widget.artitem.artitem_path,
            height: MediaQuery.of(context).size.width,
            width: MediaQuery.of(context).size.width,
            alignment: Alignment.center,
            fit: BoxFit.cover,
          ),
           SizedBox(height: 10),
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
    changeLikeState();
  }

  commentButtonPressed() {
    print("comment button pressed");
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) =>  CommentPage(artitem:widget.artitem)),
    );
  }

  purchaseButtonPressed() {
    print("purchase button pressed");
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) =>  ArtItemPage(artitem: widget.artitem)),
    );
  }
}
