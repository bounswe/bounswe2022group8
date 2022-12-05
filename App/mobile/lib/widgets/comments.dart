import 'package:artopia/comment_page.dart';
import 'package:comment_tree/comment_tree.dart';
import 'package:artopia/utils/textUtils.dart';
import 'package:artopia/utils/colorPalette.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'dart:math';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:artopia/variables.dart' ;

import '../getimage.dart';
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
          padding: const EdgeInsets.symmetric(vertical: 8, horizontal: 16),
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
                        children: [
                          const SizedBox(
                            width: 8,
                          ),
                          const Text(''),
                          const SizedBox(
                            width: 8,
                          ),
                          SizedBox(
                            width: 45,
                            height: 33,
                            child: buildTextButton("Like", Colors.white54, () => print("like")),
                          ),
                          const SizedBox(
                            width: 12,
                          ),
                          // Text("Reply"),
                          SizedBox(
                            width: 55,
                            height: 33,
                            child: buildTextButton("Reply", Colors.white54, () => {}),
                          ),
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
                        children: [
                          const SizedBox(
                            width: 8,
                          ),
                          const Text(''),
                          const SizedBox(
                            width: 8,
                          ),
                          SizedBox(
                            width: 45,
                            height: 33,
                            child: buildTextButton("Like", Colors.white54, () => print("like")),
                          ),
                          const SizedBox(
                            width: 12,
                          ),
                          // Text("Reply"),
                          SizedBox(
                            width: 55,
                            height: 33,
                            child: buildTextButton("Reply", Colors.white54, () => print("Reply")),
                          ),
                          const SizedBox(
                            width: 12,
                          ),
                          // Text("Reply"),
                          SizedBox(
                            width: 55,
                            height: 33,
                            child: buildTextButton("", Colors.white54, () => print("Edit")),
                          ),
                          const SizedBox(
                            width: 12,
                          ),
                          // Text("Reply"),
                          SizedBox(
                            width: 60,
                            height: 33,
                            child: buildTextButton("", Colors.white54, () => print("Delete")),
                          ),
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

//create a function that returns a textbutton
Widget buildTextButton(String text, Color color, Function() onPressed) {
  return TextButton(

    onPressed: onPressed,
    child: Text(
      text,
      style: GoogleFonts.inter(
        fontSize: 14,
        color: color,
      ),
    ),
  );
}

Future <List<List<Comment>>> getComments(artItemId) async {
   String GET_COMMENTS_ENDPOINT = "http://34.125.134.88:8000/api/v1/artitems/$artItemId/comments/" ;

  final response = await http.get(
    Uri.parse(GET_COMMENTS_ENDPOINT),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',      
      'Authorization': 'Token ' + token ,

    },
    )
  ;
  print(response.statusCode) ;
  //print(response.body) ;      
  
  var commentsJson = jsonDecode(response.body)['data'] as List;

  List<getCommentsClass> commentObjs = commentsJson.map((commentJson) => getCommentsClass.fromJson(commentJson)).toList();
  print(commentsJson);

  List<List<Comment>> allcomments = [] ;
  if (response.statusCode == 200) {
for (var element in commentObjs) {
      print("commentobjs") ;

  if (element.parent == 0){
    
    List<Comment> branch = [] ;
    print("parent") ;
    String profileUrl = await getImage(element.commented_by.profile_path);

    branch.add(Comment(avatar: profileUrl,content:element.body ,userName: element.commented_by.username) 
) ;
    for (var childElement in commentObjs) {
      if(childElement.parent == element.id){
            print("child") ;
    String profileUrl = await getImage(childElement.commented_by.profile_path);
    branch.add(Comment(avatar: profileUrl,content:childElement.body ,userName: childElement.commented_by.username)) ;

      } 
  }
  allcomments.add(branch) ;
}}
}

    return allcomments ;
}

class getCommentsClass{

      int id;
      String body;
      int parent ;
      CommentUserClass commented_by;
      int commented_on;
      String created_at;
      int lft;
      int rght;
      int tree_id;
      int level;
      getCommentsClass(this.id,this.body,this.parent,this.commented_by,this.commented_on,this.created_at,this.lft,this.rght,this.tree_id,this.level) ;
    factory getCommentsClass.fromJson(dynamic json) {
    return getCommentsClass(json['id'], json['body'],(json['parent']??0),CommentUserClass.fromJson(json['commented_by']), json['commented_on'], json['created_at'], json['lft'],json['rght'] ,json['tree_id'], json['level']);
  }
    }
class CommentUserClass{

      int id;
      String username;
      String profile_path;
  
      CommentUserClass(this.id,this.username,this.profile_path) ;
    factory CommentUserClass.fromJson(dynamic json) {
    return CommentUserClass(json['id'], json['username'],json['profile_path']);
  }
    }

Future<String> postComment(artItemId,parent,comment,bool isparent) async {
   String POST_COMMENT_ENDPOINT = "http://34.125.134.88:8000/api/v1/artitems/$artItemId/comments/" ;
  final response = await http.post(
    Uri.parse(POST_COMMENT_ENDPOINT),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',      
      'Authorization': 'Token ' + token ,

    },
    body: jsonEncode(<String, String>{
      'body': comment,

    },
    )
  );
    print(response.statusCode) ;
  print(response.body) ;    
  if(response.statusCode == 201){
    return "OK" ;
  }
  return "Error" ;
}