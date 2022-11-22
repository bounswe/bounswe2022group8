import 'package:flutter/material.dart';

class PostsList extends StatefulWidget {
  @override
  State<PostsList> createState() => _PostsListState();
}

class _PostsListState extends State<PostsList> {
  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.only(bottom: 10),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Padding(
            padding: const EdgeInsets.only(top: 10, left: 10, right: 10),
            child: Row(
              // mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: const [
                CircleAvatar(
                  radius: 20,
                  backgroundImage: AssetImage("assets/images/profile.jpeg"),
                ),
                SizedBox(
                  width: 10,
                ),
                Text(
                  "Selin Cihangirli",
                  style: TextStyle(
                    color: Colors.black,
                    fontFamily: "OpenSans",
                    fontSize: 16,
                    fontWeight: FontWeight.bold,
                  ),
                )
              ],
            ),
          ),
          const SizedBox(height: 10),
          Image.asset("assets/images/profile.jpeg",
              height: 500, fit: BoxFit.fill),
          const SizedBox(height: 10),
          Padding(
            padding: const EdgeInsets.only(left: 10, right: 10),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Row(
                  children: const [
                    Icon(
                      Icons.heart_broken_rounded,
                      size: 30,
                    ),
                    Padding(
                      padding: EdgeInsets.only(left: 15, right: 15),
                      child: Icon(Icons.message, size: 30),
                    ),
                    Icon(
                      Icons.attach_money,
                      size: 30,
                    ),
                  ],
                ),
              ],
            ),
          ),
          Container(
            margin: const EdgeInsets.only(left: 10, right: 10, top: 10),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text(
                  "1,3m views",
                  style: TextStyle(
                    color: Colors.black,
                    fontFamily: "OpenSans",
                    fontSize: 14,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 5),
                Row(
                  children: const [
                    Text(
                      "selincihangirli34",
                      style: TextStyle(
                        color: Colors.black,
                        fontFamily: "OpenSans",
                        fontSize: 14,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    Text(
                      " Hi! New profile picture. #NewYearNewMe",
                      style: TextStyle(
                        color: Colors.black,
                        fontFamily: "OpenSans",
                        fontSize: 14,
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 5),
                const Text(
                  "View all 1321 comments.",
                  style: TextStyle(
                    color: Colors.grey,
                    fontFamily: "OpenSans",
                    fontSize: 14,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
