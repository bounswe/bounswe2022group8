import 'package:artopia/search_page.dart';
import 'package:flutter/material.dart';

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
        //query = "";
        close(context, query);
      },
    );
  }
  @override
  Widget buildResults(BuildContext context) {
    final List<String> allUsers = listToSearch.where(
            (anUser) => anUser.toLowerCase().contains(
                query.toLowerCase(),
            ),
    ).toList();
    return ListView.builder(
      itemCount: allUsers.length,
      itemBuilder: (context, index) => ListTile(
          title: Text(allUsers[index]),
        onTap: () {
          query = allUsers[index];
          close(context, query);
        },
        ),
    );

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