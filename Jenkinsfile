#!/bin/sh
pipeline {
    agent any
    stages {
      stage('Build') {
          steps {
              echo 'Building..'
              git 'https://github.com/tongquang126/Firewall-Management.git'
                }
              }
   stage('Test') {
      steps {
          echo 'Testing..'
          sh 'python3 Hello_World.py'
            }
          }
          }
        }
      
