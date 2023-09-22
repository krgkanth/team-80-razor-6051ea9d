*** Settings ***
Documentation     I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template     Move character
Library           MoveLibrary.py

*** Test Cases ***                  StartingX     StartingY     StartingMoveCount     Direction     EndingX     EndingY     EndingMoveCount
Move in the middle of the board     0             0             1                     NORTH         0           1           2
Move on the edge of the board       0             0             5                     SOUTH         0           0           6
Moving NORTH                        0             0             1                     NORTH         0           1           2
Moving EAST                         0             0             1                     EAST          1           0           2
Moving WEST                       0             0             1                     WEST          0           0           2
Moving NORTH                      0             9             1                     NORTH         0           9           2
Moving SOUTH                      0             9             1                     SOUTH         0           8           2
Moving EAST                       0             9             1                     EAST          1           9           2
Moving WEST                       0             9             1                     WEST          0           9           2
Moving NORTH                      9             0             1                     NORTH         9           1           2
Moving SOUTH                      9             0             1                     SOUTH         9           0           2
Moving EAST                       9             0             1                     EAST          9           0           2
Moving WEST                       9             0             1                     WEST          8           0           2
Moving NORTH                      9             9             1                     NORTH         9           9           2
Moving SOUTH                      9             9             1                     SOUTH         9           8           2
Moving EAST                       9             9             1                     EAST          9           9           2



*** Keywords ***
Move character
    [Arguments]    ${startingX}    ${startingY}    ${startingMoveCount}    ${direction}    ${endingX}    ${endingY}    ${endingMoveCount}
    Initialize character xposition with  ${startingX}
    Initialize character yposition with  ${startingY}
    Initialize character moveCount with  ${startingMoveCount}
    Move in direction                    ${direction}
    Character xposition should be        ${endingX}
    Character yposition should be        ${endingY}
    Character moveCount should be        ${endingMoveCount}