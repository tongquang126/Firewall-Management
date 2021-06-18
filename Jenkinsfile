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
          sh 'python3 Execute_Button.py'
            }
          }
   stage('Report') {
      steps {
          cucumber failedFeaturesNumber: -1, failedScenariosNumber: -1, failedStepsNumber: -1, fileIncludePattern: '**/*.json', pendingStepsNumber: -1, skippedStepsNumber: -1, sortingMethod: 'ALPHABETICAL', undefinedStepsNumber: -1
            }
          }
        }
      }
