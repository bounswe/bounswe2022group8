import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:text_selection_controls/text_selection_controls.dart';
import '../utils/colorPalette.dart';

class Annotation {
  String annotationMessage;
  int annotationX;
  int annotationY;

  Annotation(this.annotationMessage, this.annotationX, this.annotationY);
}

class AnnotableTextField extends StatefulWidget {
  final String descriptionText;
  const AnnotableTextField({Key? key, required this.descriptionText})
      : super(key: key);

  @override
  State<AnnotableTextField> createState() => _AnnotableTextFieldState();
}

class _AnnotableTextFieldState extends State<AnnotableTextField> {
  final ColorPalette colorPalette = ColorPalette();

  @override
  Widget build(BuildContext context) {
    List<TextSpan> chars = [];

    for (int i = 0; i < widget.descriptionText.length; i++) {
      chars.add(TextSpan(
        text: widget.descriptionText[i],
      ));
    }

    AlertDialog AnnotationDialog(String substring, int annotationX, int annotationY, BuildContext context) {
      final TextEditingController _controller = TextEditingController();
      return AlertDialog(
        title: const Text("Annotation"),
        content: TextField(
          decoration: const InputDecoration(
            border: OutlineInputBorder(),
            labelText: 'Annotation',
          ),
          controller: _controller,
        ),
        actions: <Widget>[
          TextButton(
            child: const Text("Cancel"),
            onPressed: () {
              Navigator.of(context).pop();
            },
          ),
          TextButton(
            child: const Text("Submit"),
            onPressed: () {
              print(substring);
              print(_controller.text);
              Navigator.of(context).pop();
              //TODO: Add annotation to the database
            },
          ),
        ],
      );
    }

    return SelectableText.rich(
      TextSpan(
        children: chars,
        style: GoogleFonts.inter(
          fontSize: 20,
          color: colorPalette.blackShadows,
          fontWeight: FontWeight.w600,
        ),
      ),
      // selectionControls: MyMaterialTextSelectionControls(),
      selectionControls: FlutterSelectionControls(toolBarItems: [
        ToolBarItem(
            item: const Text(
              'Select All',
            ),
            itemControl: ToolBarItemControl.selectAll),
        ToolBarItem(
            item: const Text(
              'Copy',
            ),
            itemControl: ToolBarItemControl.copy),
        ToolBarItem(
          item: const Text(
            'Annotate',
          ),
          onItemPressed: (String substring, int annotationX, int annotationY) {
            showDialog(
                context: context,
                builder: (BuildContext context) {
                  return AnnotationDialog(substring, annotationX, annotationY,
                      context);
                });
          },
        ),
      ]),
    );
  }
}

/*

class MyMaterialTextSelectionControls extends MaterialTextSelectionControls {
  // Padding between the toolbar and the anchor.
  static const double _kToolbarContentDistanceBelow = 10.0;
  static const double _kToolbarContentDistance = 8.0;

  /// Builder for material-style copy/paste text selection toolbar.
  @override
  Widget buildToolbar(
      BuildContext context,
      Rect globalEditableRegion,
      double textLineHeight,
      Offset selectionMidpoint,
      List<TextSelectionPoint> endpoints,
      TextSelectionDelegate delegate,
      ClipboardStatusNotifier? clipboardStatus,
      Offset? lastSecondaryTapDownPosition,
      ) {
    final TextSelectionPoint startTextSelectionPoint = endpoints[0];
    final TextSelectionPoint endTextSelectionPoint =
    endpoints.length > 1 ? endpoints[1] : endpoints[0];
    final Offset anchorAbove = Offset(
      globalEditableRegion.left + selectionMidpoint.dx,
      globalEditableRegion.top +
          startTextSelectionPoint.point.dy -
          textLineHeight -
          _kToolbarContentDistance,
    );
    final Offset anchorBelow = Offset(
      globalEditableRegion.left + selectionMidpoint.dx,
      globalEditableRegion.top +
          endTextSelectionPoint.point.dy +
          _kToolbarContentDistanceBelow,
    );
    final value = delegate.textEditingValue;
    return MyTextSelectionToolbar(
      anchorAbove: anchorAbove,
      anchorBelow: anchorBelow,
      clipboardStatus: clipboardStatus,
      handleCustomButton: () {
        print(value.selection.textInside(value.text));
        delegate.hideToolbar();
      },
    );
  }
}

class MyTextSelectionToolbar extends StatelessWidget {
  const MyTextSelectionToolbar({
    Key? key,
    required this.anchorAbove,
    required this.anchorBelow,
    required this.clipboardStatus,
    required this.handleCustomButton,
  }) : super(key: key);

  final Offset anchorAbove;
  final Offset anchorBelow;
  final ClipboardStatusNotifier? clipboardStatus;
  final VoidCallback? handleCustomButton;

  @override
  Widget build(BuildContext context) {
    assert(debugCheckHasMaterialLocalizations(context));

    final List<_TextSelectionToolbarItemData> items =
    <_TextSelectionToolbarItemData>[
      _TextSelectionToolbarItemData(
        onPressed: handleCustomButton ?? () {},
        label: 'Custom button',
      ),
    ];

    int childIndex = 0;
    return TextSelectionToolbar(
      anchorAbove: anchorAbove,
      anchorBelow: anchorBelow,
      toolbarBuilder: (BuildContext context, Widget child) =>
          Container(color: Colors.pink, child: child),
      children: items
          .map((_TextSelectionToolbarItemData itemData) =>
          TextSelectionToolbarTextButton(
            padding: TextSelectionToolbarTextButton.getPadding(
                childIndex++, items.length),
            onPressed: itemData.onPressed,
            child: Text(itemData.label),
          ))
          .toList(),
    );
  }
}

class _TextSelectionToolbarItemData {
  const _TextSelectionToolbarItemData({
    required this.label,
    required this.onPressed,
  });

  final String label;
  final VoidCallback onPressed;
}

 */
