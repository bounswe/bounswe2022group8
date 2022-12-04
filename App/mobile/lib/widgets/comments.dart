import 'package:comment_tree/comment_tree.dart';
import 'package:artopia/utils/textUtils.dart';
import 'package:artopia/utils/colorPalette.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class Comments extends StatefulWidget {
  final List<Comment> commentList;

  const Comments({Key? key, required this.commentList}) : super(key: key);

  @override
  State<Comments> createState() => _CommentsState();
}

class _CommentsState extends State<Comments> {
  bool reply = false;
  var lineWidth = 3.0;
  final textUtils = TextUtils();
  final ColorPalette colorPalette = ColorPalette();

  //a function that returns first element of a commentlist
  Comment getFirstComment(List<Comment> commentList) {
    return commentList[0];
  }

  //a function that returns a list of comments that are replies to a comment
  List<Comment> getReplies(List<Comment> commentList) {
    List<Comment> replies = [];
    if(commentList.length == 1) {
      lineWidth = 0;
      return replies;
    }
    for (var i = 1; i < commentList.length; i++) {
        replies.add(commentList[i]);
    }
    return replies;
  }


  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Container(
          padding: const EdgeInsets.symmetric(vertical: 12, horizontal: 16),
          child: CommentTreeWidget<Comment, Comment>(
            // Root comment
            getFirstComment(widget.commentList),
            // Replies -Child comments-
            getReplies(widget.commentList),

            // Tree Theme api call da editlenmeyecek
            treeThemeData: TreeThemeData(lineColor: Colors.blue, lineWidth: lineWidth),

            //
            avatarRoot: (context, data) => PreferredSize(
              preferredSize: const Size.fromRadius(18),
              child: CircleAvatar(
                  radius: 26,
                  backgroundColor: Colors.white,
                  child: CircleAvatar(
                    backgroundImage: NetworkImage(
                        data.avatar!
                    ),
                    radius: 24,
                  ),
              ),
            ),
            avatarChild: (context, data) => PreferredSize(
              preferredSize: const Size.fromRadius(12),
              child: CircleAvatar(
                  radius: 18,
                  backgroundColor: Colors.grey,
                  child: CircleAvatar(
                  backgroundImage: NetworkImage(
                      data.avatar!
                  ),
                  radius: 16,
                ),
              ),
            ),
            contentChild: (context, data) {
              return Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Container(
                    padding:
                    const EdgeInsets.symmetric(vertical: 8, horizontal: 8),
                    decoration: BoxDecoration(
                        color: Colors.grey[100],
                        borderRadius: BorderRadius.circular(12)),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        textUtils.buildText(
                            '${data.userName}', 14, Colors.black, FontWeight.w600),
                        const SizedBox(
                          height: 4,
                        ),
                        textUtils.buildText(
                            '${data.content}', 14, Colors.black, FontWeight.w400),
                      ],
                    ),
                  ),
                  DefaultTextStyle(
                    style: GoogleFonts.inter(
                      fontSize: 13,
                      color: Colors.white54,
                    ),

                    child: Padding(
                      padding: const EdgeInsets.only(top: 4),
                      child: Row(
                        children: const [
                          SizedBox(
                            width: 8,
                          ),
                          Text('5d'),
                          SizedBox(
                            width: 8,
                          ),
                          Text('Like'),
                          SizedBox(
                            width: 12,
                          ),
                          Text('Reply'),
                        ],
                      ),
                    ),
                  )
                ],
              );
            },
            contentRoot: (context, data) {
              return Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Container(
                    padding:
                    const EdgeInsets.symmetric(vertical: 8, horizontal: 8),
                    decoration: BoxDecoration(
                        color: Colors.grey[100],
                        borderRadius: BorderRadius.circular(12)),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        textUtils.buildText(
                            '${data.userName}', 15, Colors.black, FontWeight.w600),
                        const SizedBox(
                          height: 4,
                        ),
                        textUtils.buildText(
                            '${data.content}', 15, Colors.black, FontWeight.w400),
                      ],
                    ),
                  ),
                  DefaultTextStyle(
                    style: GoogleFonts.inter(
                      fontSize: 13,
                      color: Colors.white54,
                    ),
                    child: Padding(
                      padding: const EdgeInsets.only(top: 4),
                      child: Row(
                        children: const [
                          SizedBox(
                            width: 8,
                          ),
                          Text('5d'),
                          SizedBox(
                            width: 8,
                          ),
                          Text('Like'),
                          SizedBox(
                            width: 12,
                          ),
                          Text('Reply'),
                        ],
                      ),
                    ),
                  )
                ],
              );
            },
          ),
        ),
      ],
    );
  }
}