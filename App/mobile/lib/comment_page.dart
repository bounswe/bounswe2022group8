import 'utils/colorPalette.dart';
import 'utils/textUtils.dart';
import 'widgets/comments.dart';
import 'package:flutter/material.dart';
import 'package:comment_tree/comment_tree.dart';
import 'package:flutter/services.dart';

import 'artitem.dart';
import 'home_page.dart';

class CommentPage extends StatefulWidget {
  final ArtItem artitem ;

  const CommentPage({Key? key, required this.artitem}) : super(key: key);

  @override
  State<CommentPage> createState() => _CommentPageState();
}

class _CommentPageState extends State<CommentPage> {
  bool replyState = false;
  final textUtils = TextUtils();
  //Future<List<List<Comment>>> allcomments = getComments(this.artitem.id);
  final CommentInputObject = TextEditingController();
  final ColorPalette colorPalette = ColorPalette();
  final List<Comment> commentLi = [
    Comment(
      avatar:
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0pxYCCGBKN0MuhVp6RObFWmbeRIUNxM6YPA&usqp=CAU",
      userName: 'Mustafa Cihan',
      content:
          'Flutter Comment Tree eklentisi ile yaptim. Ilk comment her zaman root comment olacak.',
    ),
    Comment(
      avatar:
          'https://static.wikia.nocookie.net/reddeadredemption/images/8/87/RDR2_Dutch_van_der_Linde_PC.png/revision/latest?cb=20191216204516',
      userName: 'Dogukan Turksoy',
      content:
          'Api ile baglanti kurup commentleri cekmek lazim. Tree derinligi 1den buyuk yapamadim.',
    ),
    Comment(
      avatar:
          'https://www.giantbomb.com/a/uploads/square_medium/5/56742/3058980-7283848050-rdr2-.jpg',
      userName: 'Mustafa Emre Erengul',
      content: 'Lutfen bu olsun artik cunku.',
    ),
    Comment(
      avatar:
          'https://static.wikia.nocookie.net/reddeadfanon/images/0/09/Micah_Bell_1906.png/revision/latest?cb=20200210183833',
      userName: 'Metehan Dundar',
      content: 'Sanirim oldu bilmiyorum oldu mu olmadi mi?.',
    ),
  ];
  final List<Comment> commentHi = [
    Comment(
      avatar:
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0pxYCCGBKN0MuhVp6RObFWmbeRIUNxM6YPA&usqp=CAU",
      userName: 'Mustafa Cihan',
      content:
          'Flutter Comment Tree eklentisi ile yaptim. Ilk comment her zaman root comment olacak.',
    )
  ];
  final List<Comment> commentMid = [
    Comment(
      avatar:
          'https://www.giantbomb.com/a/uploads/square_medium/5/56742/3058980-7283848050-rdr2-.jpg',
      userName: 'Mustafa Emre Erengul',
      content: 'Commentler bu sekilde gozukuyor.',
    ),
  ];
  final List<Comment> comment = [
    Comment(
      avatar:
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0pxYCCGBKN0MuhVp6RObFWmbeRIUNxM6YPA&usqp=CAU",
      userName: 'Mustafa Cihan',
      content: 'AAAAAAAAAAAAAAAAAAAA',
    ),
  ];

  void _update(bool value) {
    setState(() => replyState = value);
  }

  @override
  Widget build(BuildContext context) {
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
            },
          ),
          title: textUtils.buildText(
              "Comments", 25, Colors.white70, FontWeight.w500),
        ),
      ),
      body: AnnotatedRegion<SystemUiOverlayStyle>(
        value: SystemUiOverlayStyle.light,
        child: GestureDetector(
          onTap: () => FocusScope.of(context).unfocus(),
          child: Column(
            children: [
              Expanded(
                child: Container(
                  color: Colors.black,
                  child: SingleChildScrollView(
                      scrollDirection: Axis.vertical,
                      child: FutureBuilder<List<List<Comment>>>(
                          future: getComments(widget.artitem.id),
                          builder: (BuildContext context,
                              AsyncSnapshot<List<List<Comment>>> snapshot) {
                            if (snapshot.hasData == false)
                              return SizedBox.shrink();
                            List<List<Comment>> artItemcomments =
                                snapshot.requireData;
                            List<Comments> commentWidgets = [];

                            for (var element in artItemcomments)
                              commentWidgets
                                  .add(Comments(commentList: element));
                            return Column(
                              children: commentWidgets,
                            );
                          })),
                ),
              ),
              ListTile(
                title: TextFormField(
                  controller: CommentInputObject,
                  style: TextStyle(color: Colors.white),
                  decoration: const InputDecoration(
                    labelText: "Add a comment...",
                    labelStyle: TextStyle(color: Colors.white),
                    border: InputBorder.none,
                  ),
                ),
                trailing: OutlinedButton(
                  style: OutlinedButton.styleFrom(
                    backgroundColor: colorPalette.russianGreen,
                  ),
                  onPressed: () {
                    String comment = CommentInputObject.text;
                    postComment(widget.artitem.id, 1, comment, true).then((value) {
                      if (value == "OK") {
                        Navigator.pushReplacement(
                          context,
                          MaterialPageRoute(
                              builder: (context) => CommentPage(artitem: widget.artitem)),
                        );
                      }
                    });
                  },
                  child: textUtils.buildText("Post", 18,
                      colorPalette.palePurplePantone, FontWeight.w500),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
