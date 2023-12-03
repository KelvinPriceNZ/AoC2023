#!/bin/bash

for day in {01..25}
do
   if [ -d $day ]
   then
      for part in 1 2
      do
         soln="${day}/part${part}.py"
         if [ $part -eq 1 ]
         then
            echo -n "Day $day "
         else
            echo -n "       "
         fi
         echo -n "Part $part : "
         if [ -s ${soln} -a -x $soln ]
         then
            $soln
         else
            echo "*Unsolved*"
         fi
      done
   fi
done
