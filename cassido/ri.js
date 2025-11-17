#!/usr/bin/env node
"use strict";
/*
This week's (2025-11-17) question:
Given a positive integer n, write a function that returns an array containing all integers from 1 to n, where each integer i appears exactly i times in the result. For example, 3 should appear 3 times, 5 should appear 5 times, and so on. The order of the integers in the output array does not matter.
*/

function repeatedIntegers(n) {
  const result = [];
  for (let i = 1; i <= n; i++) {
    for (let j = 0; j < i; j++) {
      result.push(i);
    }
  }
  return result;
}

if (require.main === module) {
  // CLI: print the result for n=4 (same as the Python script)
  // Use JSON.stringify so the array prints nicely
  console.log(repeatedIntegers(4));
}

module.exports = { repeatedIntegers };
