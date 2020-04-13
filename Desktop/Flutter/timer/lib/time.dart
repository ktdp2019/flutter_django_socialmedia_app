import 'package:flutter/material.dart';
import 'dart:async';


class AppTime extends StatefulWidget {

  @override
  _AppTimeState createState() => _AppTimeState();

}


class _AppTimeState extends State<AppTime> {

  String _timeString;

  @override
  void initState(){
    _timeString = "${DateTime.now().hour} : ${DateTime.now().minute} :${DateTime.now().second}";
    Timer.periodic(Duration(seconds:1), (Timer t)=>_getCurrentTime());
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Fluter Test'),),
      body:Center(
        child: Text(_timeString, style: TextStyle(fontSize: 30),),
      ),
    );
  }

  void _getCurrentTime()  {
    setState(() {
      _timeString = "${DateTime.now().hour} : ${DateTime.now().minute} :${DateTime.now().second}";
    });
  }

}