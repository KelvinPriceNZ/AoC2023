#!/bin/bash

for day in {01..25}
do
   if [ -d $day ]
   then
      for part in 1 2
      do
         soln="${day}/part${part}.py"
         echo -n "Day $day Part $part : "
         if [ -s ${soln} -a -x $soln ]
         then
            $soln
         else
            echo "*Unsolved*"
         fi
      done
   fi
done
