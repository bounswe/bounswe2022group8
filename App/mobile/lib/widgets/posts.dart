import 'package:flutter/material.dart';
import 'package:artopia/utils/colorPalette.dart';
import 'package:artopia/utils/textUtils.dart';

class PostsList extends StatefulWidget {
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
      decoration: BoxDecoration(
        color: colorPalette.palatinatePurple,
      ),
      alignment: Alignment.topCenter,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Padding(
            padding: const EdgeInsets.only(left: 5, top: 7),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children:  [
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
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Row(
                  children: [
                    Icon(
                      Icons.heart_broken_rounded,
                      color: colorPalette.blackShadows,
                      size: 30,
                    ),
                    const Padding(
                      padding: EdgeInsets.only(right: 5),
                    ),
                    Icon(
                          Icons.message,
                          color: colorPalette.blackShadows,
                          size: 30),
                    const Padding(
                      padding: EdgeInsets.only(right: 5),
                    ),
                    Icon(
                      Icons.attach_money,
                      color: colorPalette.blackShadows,
                      size: 30,
                    ),
                  ],
                ),
              ],
            ),
          ),
          // Container(
          //   margin: const EdgeInsets.only(left: 10, right: 10, top: 10),
          //   child: Column(
          //     crossAxisAlignment: CrossAxisAlignment.start,
          //     children: [
          //       const Text(
          //         "1,3m views",
          //         style: TextStyle(
          //           color: Colors.black,
          //           fontFamily: "OpenSans",
          //           fontSize: 14,
          //           fontWeight: FontWeight.bold,
          //         ),
          //       ),
          //       const SizedBox(height: 5),
          //       Row(
          //         children: const [
          //           Text(
          //             "selincihangirli34",
          //             style: TextStyle(
          //               color: Colors.black,
          //               fontFamily: "OpenSans",
          //               fontSize: 14,
          //               fontWeight: FontWeight.bold,
          //             ),
          //           ),
          //           Flexible(
          //             child: Text(
          //               " Hi! New profile picture. #NewYearNewMe",
          //               style: TextStyle(
          //                 color: Colors.black,
          //                 fontFamily: "OpenSans",
          //                 fontSize: 14,
          //               ),
          //             ),
          //           ),
          //         ],
          //       ),
          //       const SizedBox(height: 5),
          //       const Text(
          //         "View all 1321 comments.",
          //         style: TextStyle(
          //           color: Colors.grey,
          //           fontFamily: "OpenSans",
          //           fontSize: 14,
          //         ),
          //       ),
          //     ],
          //   ),
          // ),
        ],
      ),
    );
  }
}
