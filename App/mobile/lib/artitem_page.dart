import 'package:artopia/widgets/post.dart';
import 'package:flutter/material.dart';
import 'package:artopia/utils/textUtils.dart';
import 'package:artopia/utils/colorPalette.dart';
import 'package:flutter/services.dart';
import 'artitem.dart';
import 'comment_page.dart';
import 'home_page.dart';

class ArtItemPage extends StatefulWidget {
  final ArtItem artitem ;

  //Post classinin icinden acildigi icin
  const ArtItemPage({Key? key, required this.artitem}) : super(key: key);

  @override
  State<ArtItemPage> createState() => _ArtItemPageState();
}

class _ArtItemPageState extends State<ArtItemPage> {
  final textUtils = TextUtils();
  final ColorPalette colorPalette = ColorPalette();

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
      tooltip: 'Purchase',
      onPressed: () => {purchaseButtonPressed()},
    );
    return Scaffold(
      backgroundColor: Colors.black,
      // backgroundColor: colorPalette.darkPurple,
      appBar: PreferredSize(
        preferredSize: const Size.fromHeight(40.0),
        child: AppBar(
          backgroundColor: colorPalette.darkPurple,
          leading: BackButton(
            color: Colors.white,
            onPressed: () => {
              Navigator.pop(
                context,
                MaterialPageRoute(builder: (context) => HomePage()),
              )
            }
          ),
        ),
      ),
      body: SingleChildScrollView(
        child: AnnotatedRegion<SystemUiOverlayStyle>(
          value: SystemUiOverlayStyle.light,
          child: GestureDetector(
            onTap: () => FocusScope.of(context).unfocus(),
            child: Column(
              children: [
                Post(artitem: widget.artitem).createArtItemPage(),
              ],
            ),
          ),
        ),
      ),
      bottomNavigationBar: BottomAppBar(
        color: colorPalette.darkPurple,
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceEvenly,
          children: [
            likeButton,
            commentButton,
            purchaseButton
          ],
        ),
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
      MaterialPageRoute(builder: (context) =>  CommentPage(artitem: widget.artitem)),
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
