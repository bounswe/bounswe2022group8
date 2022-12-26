import 'package:artopia/search_page.dart';
import 'package:flutter/material.dart';

class Search extends SearchDelegate<String>{
  final List<String> allCaliforniaPlaces;
  final List<String> californiaPlaceSuggestion;
  Search({required this.allCaliforniaPlaces, required this.californiaPlaceSuggestion});
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
    final List<String> allLocations = allCaliforniaPlaces.where(
            (californiaPlace) => californiaPlace.toLowerCase().contains(
                query.toLowerCase(),
            ),
    ).toList();
    return ListView.builder(
      itemCount: allLocations.length,
      itemBuilder: (context, index) => ListTile(
          title: Text(allLocations[index]),
        onTap: () {
          query = allLocations[index];
          close(context, query);
        },
        ),
    );

  }
  @override

  Widget buildSuggestions(BuildContext context) {
    final List<String> locationSuggestions = californiaPlaceSuggestion.where(
          (placeSuggestions) => placeSuggestions.toLowerCase().contains(
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