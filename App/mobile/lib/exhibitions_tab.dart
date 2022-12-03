import 'package:flutter/material.dart';
import 'package:artopia/profile.dart';
import 'package:artopia/utils/colorPalette.dart';
import 'package:artopia/utils/textUtils.dart';
import 'package:artopia/widgets/post.dart';
import 'package:artopia/comment_page.dart';

class Exhibitions extends StatefulWidget {
  @override
  _Exhibitions createState() => _Exhibitions();
}

class _Exhibitions extends State<Exhibitions> {
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
  final ColorPalette colorPalette = ColorPalette();
  final textUtils = TextUtils();
  late OverlayEntry _popupDialog;
  List<String> imageUrls = [
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: colorPalette.palePurplePantone,
      body: GridView.count(
        crossAxisCount: 3,
        childAspectRatio: 1.0,
        children: imageUrls.map(_createGridTileWidget).toList(),
      ),
    );
  }

  Widget _createGridTileWidget(String url) => Builder(
    builder: (context) => GestureDetector(
      onLongPress:() {
        _popupDialog = _createPopupDialog(url);
        Overlay.of(context)?.insert(_popupDialog);
      },
      onLongPressEnd: (details) => _popupDialog.remove(),
      child: Image.network(url, fit: BoxFit.cover),
    ),
  );

  OverlayEntry _createPopupDialog(String url) {
    return OverlayEntry(
      builder: (context) => AnimatedDialog(
        child: _createPopupContent(url),
      ),
    );
  }
  Widget _createPhotoTitle() => Container(
      width: double.infinity,
      color: colorPalette.blackShadows,
      child: ListTile(
        leading: CircleAvatar(
          backgroundImage: Image.asset("assets/images/blank_profile.jpeg").image,
        ),
        title: Text(
          'selin',
          style: TextStyle(color: Colors.black, fontWeight: FontWeight.w600),
        ),
      ));

  Widget _createActionBar() => Container(
    padding: EdgeInsets.symmetric(vertical: 10.0),
    color: colorPalette.blackShadows,
    child: Row(
      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
      children: [
        IconButton(
          icon: const Icon(
            Icons.favorite,
            color: Colors.black,
          ),
          onPressed: () => likeButtonPressed(),
        ),
        IconButton(
          icon: const Icon(
            Icons.chat,
            color: Colors.black,
          ),
          onPressed: () => commentButtonPressed(),
        ),
        IconButton(
          icon: const Icon(
            Icons.attach_money,
            color: Colors.black,
          ),
          onPressed: () => print("money button pressed"),
        ),
      ],
    ),
  );

  Widget _createPopupContent(String url) => Container(
    padding: EdgeInsets.symmetric(horizontal: 16.0),
    child: ClipRRect(
      borderRadius: BorderRadius.circular(16.0),
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          //_createPhotoTitle(),
          Image.network(url, fit: BoxFit.fitWidth),
          //_createActionBar(),
        ],
      ),
    ),
  );
}

class AnimatedDialog extends StatefulWidget {
  const AnimatedDialog({Key? key, required this.child}) : super(key: key);

  final Widget child;

  @override
  State<StatefulWidget> createState() => AnimatedDialogState();
}

class AnimatedDialogState extends State<AnimatedDialog>
    with SingleTickerProviderStateMixin {
  late AnimationController controller;
  late Animation<double> opacityAnimation;
  late Animation<double> scaleAnimation;

  @override
  void initState() {
    super.initState();

    controller = AnimationController(
        vsync: this, duration: const Duration(milliseconds: 400));
    scaleAnimation =
        CurvedAnimation(parent: controller, curve: Curves.easeOutExpo);
    opacityAnimation = Tween<double>(begin: 0.0, end: 0.6).animate(
        CurvedAnimation(parent: controller, curve: Curves.easeOutExpo));

    controller.addListener(() => setState(() {}));
    controller.forward();
  }

  @override
  Widget build(BuildContext context) {
    return Material(
      color: Colors.black.withOpacity(opacityAnimation.value),
      child: Center(
        child: FadeTransition(
          opacity: scaleAnimation,
          child: ScaleTransition(
            scale: scaleAnimation,
            child: widget.child,
          ),
        ),
      ),
    );
  }
}
