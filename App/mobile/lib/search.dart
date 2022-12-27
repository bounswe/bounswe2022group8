import 'package:artopia/search_page.dart';
import 'package:flutter/material.dart';

import 'artitem.dart';
import 'widgets/post.dart';

class Search extends SearchDelegate<String>{
  final List<String> listToSearch;
  final List<String> listToSuggest;
  Search({required this.listToSearch, required this.listToSuggest});
  @override
  List<Widget> buildActions(BuildContext context) {
    return [
      IconButton(
        icon: Icon(Icons.clear),
        onPressed: () {
          print("user");
          query = "";
        },
      ),
    ];
  }
  @override
  Widget buildLeading(BuildContext context) {
    return IconButton(
      icon: Icon(Icons.arrow_back),
      onPressed: () {
        print("art item");

        //query = "";
        close(context, query);
      },
    );
  }
  @override
  Widget buildResults(BuildContext context) {
    return FutureBuilder<List<ArtItem>>(
          future: searchArtItems(query),
          builder: (BuildContext context,
              AsyncSnapshot<List<ArtItem>> snapshot) {
            if (snapshot.hasData == false)
              return SizedBox.shrink();
            List<ArtItem> artItems = snapshot.requireData;

            return  SingleChildScrollView(
          scrollDirection: Axis.vertical,
          child: Column(
            children: [
              for (ArtItem item in artItems ) (Post(artitem: item)),
            ],
          ),
    ) ;},);
    final List<String> allUsers = listToSearch.where(
            (anUser) => anUser.toLowerCase().contains(
                query.toLowerCase(),
            ),
    ).toList();
 

  }
  @override

  Widget buildSuggestions(BuildContext context) {
    final List<String> suggestions = listToSuggest.where(
          (aSuggestion) => aSuggestion.toLowerCase().contains(
        query.toLowerCase(),
      ),
    ).toList();
    return
      SizedBox.shrink();
      /*
      ListView.builder(
      itemCount: locationSuggestions.length,
      itemBuilder: (context, index) => ListTile(
        title: Text(locationSuggestions[index]),
        onTap: () {
          query = locationSuggestions[index];
          close(context, query);
        },
        ),
    );
    */

  }
}