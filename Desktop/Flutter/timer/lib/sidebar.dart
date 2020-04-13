import 'package:flutter/material.dart';
import 'home.dart';

class SideBar extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return new Drawer(
      child: ListView(
        children: <Widget>[
          new UserAccountsDrawerHeader(
          accountName: new Text("Amit"),
          accountEmail: null)
        ],
      ),
    );
  }
}