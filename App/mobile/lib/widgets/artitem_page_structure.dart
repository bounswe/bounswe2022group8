import 'package:artopia/artitem.dart';
import 'package:flutter/material.dart';
import '../utils/colorPalette.dart';
import '../utils/textUtils.dart';
import 'TextAnnotation.dart';
import '../variables.dart';
class ArtItemPageStructue extends StatefulWidget {
  final ArtItem artitem ;
  const ArtItemPageStructue({Key? key , required  this.artitem}) : super(key: key);

  @override
  State<ArtItemPageStructue> createState() => _ArtItemPageStructueState();
}

class _ArtItemPageStructueState extends State<ArtItemPageStructue> {
  final textUtils = TextUtils();
  final colorPalette = ColorPalette();
  bool annotationSelected = false;
  String annotationButtonString = "Show Annotations";
  @override
  Widget build(BuildContext context) {
   annotated_item_url = widget.artitem.artitem_path ;
   annotated_item_id = widget.artitem.id ;
    void changeAnnotationSelected() {
      setState(() {
        annotationSelected = !annotationSelected;
        if (annotationSelected) {
          annotationButtonString = "Hide Annotations";
        } else {
          annotationButtonString = "Show Annotations";
        }
      });
    }


    return Container(
      margin: const EdgeInsets.only(top: 5, bottom: 5),
      foregroundDecoration: BoxDecoration(
        border: Border.all(
          color: Colors.black,
          width: 4,
        ),
        borderRadius: BorderRadius.zero,
      ),
      decoration: const BoxDecoration(
        color: Colors.black,
        // color: colorPalette.palatinatePurple,
      ),
      alignment: Alignment.topCenter,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Row(
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [

              textUtils.buildText(widget.artitem.title, 28, colorPalette.blackShadows,
                  FontWeight.w600),
            ],
          ),
          const Padding(
            padding: EdgeInsets.only(left: 10, top: 10, right: 10),
          ),
          Image.network(
            widget.artitem.artitem_path,
            height: MediaQuery.of(context).size.width,
            width: MediaQuery.of(context).size.width,
            alignment: Alignment.center,
            fit: BoxFit.cover,
          ),
          // const SizedBox(height: 10),
          const Padding(
            padding: EdgeInsets.only(bottom: 10),
          ),
          Row(
            crossAxisAlignment: CrossAxisAlignment.center,
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Row(
                children: [
                  const SizedBox(
                    width: 15,
                  ),
                   CircleAvatar(
                    radius: 25,
                    backgroundImage: Image.network( widget.artitem.profile_path).image,
                  ),
                  const SizedBox(
                    width: 10,
                  ),
                  textUtils.buildText(widget.artitem.username, 20, colorPalette.blackShadows,
                      FontWeight.w600),
                ],
              ),
              Row(
                mainAxisAlignment: MainAxisAlignment.start,
                children: [
                  textUtils.buildText("${widget.artitem.likes} likes", 13, colorPalette.blackShadows,
                      FontWeight.w600),
                  const SizedBox(
                    width: 15,
                  ),
                  TextButton(onPressed:()=>{
                    changeAnnotationSelected(),
                  }, child:
                  textUtils.buildText(annotationButtonString, 13, colorPalette.blackShadows,
                      FontWeight.w600),
                  ),
                ],
              ),
            ],
          ),
          Padding(
            padding: const EdgeInsets.only(left: 15, top: 15, right: 15,bottom: 15),
            child: AnnotableTextField(widget.artitem.description, annotationSelected),
          ),
        ],
      ),
    );
  }
}
