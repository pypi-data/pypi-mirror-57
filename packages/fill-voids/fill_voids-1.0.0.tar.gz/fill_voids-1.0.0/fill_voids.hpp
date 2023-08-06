/*
 * This file is part of fill_voids.
 * 
 * fill_voids is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * fill_voids is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with fill_voids.  If not, see <https://www.gnu.org/licenses/>.
 *
 * 
 * Author: William Silversmith
 * Affiliation: Seung Lab, Princeton University
 * Date: December 2019
 */

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdint>
#include <vector>
#include <stack>
#include <string>

#include "libdivide.h"

#ifndef FILLVOIDS_HPP
#define FILLVOIDS_HPP

#define BACKGROUND 0
#define VISITED_BACKGROUND 1
#define FOREGROUND 2

namespace fill_voids {

inline void add_neighbors(
  uint8_t* visited, std::stack<size_t> &stack,
  const size_t sxv, const size_t syv, const size_t szv, 
  const size_t cur, const size_t y, const size_t z,
  bool &yplus, bool &yminus, bool &zplus, bool &zminus
) {
  const size_t sxyv = sxv * syv;

  // Only add a seed point if we've just 
  // started OR have just passed a foreground
  // voxel.

  if (y > 0) {
    if (visited[cur-sxv]) {
      yminus = yminus || (visited[cur-sxv] == FOREGROUND);
    }
    else if (yminus) {
      stack.push( cur - sxv );
      yminus = false;
    }
  }

  if (y < syv - 1) {
    if (visited[cur+sxv]) {
      yplus = yplus || (visited[cur+sxv] == FOREGROUND);
    }
    else if (yplus) {
      stack.push( cur + sxv );
      yplus = false;
    }
  }

  if (z > 0) {
    if (visited[cur-sxyv]) {
      zminus = zminus || (visited[cur-sxyv] == FOREGROUND);
    }
    else if (zminus) {
      stack.push( cur - sxyv );
      zminus = false;
    }
  }

  if (z < szv - 1) {
    if (visited[cur+sxyv]) {
      zplus = zplus || (visited[cur+sxyv] == FOREGROUND);
    }
    else if (zplus) {
      stack.push( cur + sxyv );
      zplus = false;
    }
  }
}

template <typename T>
void _binary_fill_holes(
  T* labels, 
  const size_t sx, const size_t sy, const size_t sz
) {

  const size_t sxy = sx * sy;
  const size_t voxels = sx * sy * sz;

  if (voxels == 0) {
    return;
  }

  const size_t sxv = sx + 2;
  const size_t syv = sy + 2;
  const size_t szv = sz + 2;
  const size_t sxyv = sxv * syv;

  uint8_t* visited = new uint8_t[sxyv * szv](); 

  // paint labels into visited offset by +<1,1,1>
  // and mark all foreground as 2 (FOREGROUND) 
  // so we can mark visited as 1 (VISITED_BACKGROUND) 
  // without overwriting foreground as we want foreground 
  // to be 2 and voids to be 0 (BACKGROUND)
  for (size_t z = 0; z < sz; z++) {
    for (size_t y = 0; y < sy; y++) {
      for (size_t x = 0; x < sx; x++) {
        size_t i = x + sx * y + sxy * z;
        visited[(x+1) + sxv * (y+1) + sxyv * (z+1)] = static_cast<uint8_t>(labels[i] > 0) << 1;
      }
    }
  }

  const libdivide::divider<size_t> fast_sxv(sxv); 
  const libdivide::divider<size_t> fast_sxyv(sxyv); 

  std::stack<size_t> stack;
  stack.push(0);

  while (!stack.empty()) {
    size_t loc = stack.top();
    stack.pop();

    if (visited[loc]) {
      continue;
    }

    size_t z = loc / fast_sxyv;
    size_t y = (loc - (z * sxyv)) / fast_sxv;
    size_t startx = y * sxv + z * sxyv;

    bool yplus = true;
    bool yminus = true;
    bool zplus = true;
    bool zminus = true;

    for (size_t cur = loc; cur < startx + sxv; cur++) {
      if (visited[cur]) {
        break;
      }
      visited[cur] = VISITED_BACKGROUND;
      add_neighbors(
        visited, stack,
        sxv, syv, szv, 
        cur, y, z,
        yplus, yminus, zplus, zminus
      );
    }

    yplus = true;
    yminus = true;
    zplus = true;
    zminus = true;

    // avoid integer underflow
    for (int64_t cur = static_cast<int64_t>(loc) - 1; cur >= static_cast<int64_t>(startx); cur--) {
      if (visited[cur]) {
        break;
      }
      visited[cur] = VISITED_BACKGROUND;
      add_neighbors(
        visited, stack,
        sxv, syv, szv, 
        cur, y, z,
        yplus, yminus, zplus, zminus
      );
    }    
  }

  for (size_t z = 0; z < sz; z++) {
    for (size_t y = 0; y < sy; y++) {
      for (size_t x = 0; x < sx; x++) {
        labels[ x + sx * y + sxy * z ] = static_cast<T>(
          visited[ (x+1) + sxv * (y+1) + sxyv * (z+1) ] != VISITED_BACKGROUND
        );
      }
    }
  }

  delete[] visited;
}


};

#undef BACKGROUND
#undef VISITED_BACKGROUND
#undef FOREGROUND

#endif