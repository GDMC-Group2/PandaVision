from __future__ import annotations
from typing import Optional
from typing import List
import heapq
from typing import Callable, Dict
from time import *


class Location:
    def __init__(self, row: int, column: int) -> None:
        """
        迷路のグリッドの位置情報単体を扱うクラス。

        Parameters
        ----------
        row : int
            位置の行番号。0からスタートし、上から下に向かって1ずつ
            加算される。
        column : int
            位置の列番号。0からスタートし、左から右に向かって1ずつ
            加算される。
        """
        self.row: int = row
        self.column: int = column


class Maze:

    def __init__(self, height_map, area_map) -> None:
        self.start_loc: Location = Location(row=0, column=0)
        self.goal_loc: Location = Location(row=0, column=0)
        self._ROW_NUM: int = height_map.shape[0]
        self._COLUMN_NUM: int = height_map.shape[1]
        self.height_map = height_map
        self.area_map = area_map
        self.height_dict = {}
        self.movable_locations_2d_list = []
        for i in range(self._ROW_NUM):
            list0 = []
            for j in range(self._COLUMN_NUM):
                list0.append([])
            self.movable_locations_2d_list.append(list0)

    def set_start_and_goal_location(self, start, end) -> None:
        """
        開始地点（入口）とゴール（出口）の座標の属性を設定する。
        """
        self.start_loc: Location = Location(row=start[0], column=start[1])
        self.goal_loc: Location = Location(row=end[0], column=end[1])

    def is_goal_loc(self, location: Location) -> bool:
        """
        指定された位置がゴールの位置かどうかの真偽値を取得する。

        Parameters
        ----------
        location : Location
            判定用の位置。

        Returns
        -------
        result : bool
            ゴールの位置であればTrueが設定される。
        """
        if (location.row == self.goal_loc.row
                and location.column == self.goal_loc.column):
            return True
        return False

    def get_movable_locations(self, location: Location) -> List[Location]:
        """
        指定された位置から、移動が可能な位置のリストを取得する。

        Parameters
        ----------
        location : Location
            基準となる位置のインスタンス。

        Returns
        -------
        movable_locations : list of Location
            移動可能な位置のインスタンスを格納したリスト。
        """
        if len(self.movable_locations_2d_list[location.row][location.column]) == 0:
            movable_locations: List[Location] = []
            # 下に移動可能かどうかの判定処理。
            if location.row + 1 < self._ROW_NUM:
                is_wall: bool = True if self.area_map[location.row + 1][location.column] < -1 else False
                if not is_wall:
                    movable_locations.append(
                        Location(row=location.row + 1, column=location.column))

            # 上に移動可能かどうかの判定処理。
            if location.row - 1 >= 0:
                is_wall: bool = True if self.area_map[location.row - 1][location.column] < -1 else False
                if not is_wall:
                    movable_locations.append(
                        Location(row=location.row - 1, column=location.column))

            # 右に移動可能かどうかの判定処理。
            if location.column + 1 < self._COLUMN_NUM:
                is_wall: bool = True if self.area_map[location.row][location.column + 1] < -1 else False
                if not is_wall:
                    movable_locations.append(
                        Location(row=location.row, column=location.column + 1))

            # 左に移動可能かどうかの判定処理。
            if location.column - 1 >= 0:
                is_wall: bool = True if self.area_map[location.row][location.column - 1] < -1 else False
                if not is_wall:
                    movable_locations.append(
                        Location(row=location.row, column=location.column - 1))

            # # 左下
            # if location.row + 1 < self._ROW_NUM and location.column - 1 >= 0:
            #     is_wall: bool = True if self.area_map[location.row + 1][location.column - 1] < 0 else False
            #     if not is_wall:
            #         movable_locations.append(
            #             Location(row=location.row + 1, column=location.column - 1))
            # # 左上
            # if location.row - 1 < self._ROW_NUM and location.column - 1 >= 0:
            #     is_wall: bool = True if self.area_map[location.row - 1][location.column - 1] < 0 else False
            #     if not is_wall:
            #         movable_locations.append(
            #             Location(row=location.row - 1, column=location.column - 1))
            #
            # # 右下
            # if location.row + 1 < self._ROW_NUM and location.column + 1 >= 0:
            #     is_wall: bool = True if self.area_map[location.row + 1][location.column + 1] < 0 else False
            #     if not is_wall:
            #         movable_locations.append(
            #             Location(row=location.row + 1, column=location.column + 1))
            #
            # # 右上
            # if location.row - 1 < self._ROW_NUM and location.column + 1 >= 0:
            #     is_wall: bool = True if self.area_map[location.row - 1][location.column + 1] < 0 else False
            #     if not is_wall:
            #         movable_locations.append(
            #             Location(row=location.row - 1, column=location.column + 1))

            self.movable_locations_2d_list[location.row][location.column] = movable_locations
            return movable_locations
        else:
            return self.movable_locations_2d_list[location.row][location.column]

    def get_manhattan_distance(self, location: Location) -> int:
        """
        対象の位置と出口（ゴール）の位置間でのマンハッタン距離を
        取得する。

        Parameters
        ----------
        location : Location
            対象の位置のインスタンス。

        Returns
        -------
        distance : int
            対象の位置と出口の位置間のマンハッタン距離。列方向の
            差異の絶対値と行方向の差異の絶対値の合計が設定される。
        """
        x_distance: int = abs(location.column - self.goal_loc.column)
        y_distance: int = abs(location.row - self.goal_loc.column)
        distance: int = x_distance + y_distance
        return distance


class Node:

    def __init__(
            self, location: Location, parent: Optional[Node],
            cost: float, heuristic: float) -> None:
        """
        迷路の位置や推移の情報などを保持するためのノード単体のデータを
        扱うクラス。

        Parameters
        ----------
        location : Location
            対象の位置情報を扱うインスタンス。
        parent : Node or None
            移動前の位置情報を扱うノードのインスタンス。探索開始時
            などにはNoneとなる。
        cost : float
            開始位置から該当のノードの位置までのコスト値（g(n)で
            得られる値）。
        heuristic : float
            このノードから出口までの距離の推定値（h(n)で得られる値）。
        """
        self.location: Location = location
        self.parent: Optional[Node] = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other_node: Node) -> bool:
        """
        比較のオペレーター( < )による処理のためのメソッド。
        優先度付きキューの制御のために利用される。

        Parameters
        ----------
        other_node : Node
            比較対象となる他のノードのインスタンス。

        Returns
        -------
        result_bool : bool
            比較結果。算出処理は入口からのコスト（g(n)）と
            ヒューリスティックの値（h(n)）の合算値の比較で
            行われる。
        """
        left_value: float = self.cost + self.heuristic
        right_value: float = other_node.cost + other_node.heuristic
        result_bool: bool = left_value < right_value
        return result_bool


def get_path_from_goal_node(goal_node: Node):
    """
    出口のノードから、探索で取得できた入口 → 出口までのパスを
    取得する。

    Parameters
    ----------
    goal_node : Node
        対象の出口（ゴール）のノードのインスタンス。

    Returns
    -------
    path : list of Location
        入口から出口までの各位置のインスタンスを格納したリスト。
    """
    path: List[Location] = [goal_node.location]
    node: Node = goal_node
    while node.parent is not None:
        node = node.parent
        path.append(node.location)
    path.reverse()
    path_list = []
    for one_loc in path:
        path_list.append((one_loc.row, one_loc.column))
    return path_list


class PriorityQueue:

    def __init__(self) -> None:
        """
        優先度付きキューの制御を行うためのクラス。
        """
        self._container: List[Node] = []

    @property
    def empty(self) -> bool:
        """
        キューが空かどうかの属性値。

        Returns
        -------
        result : bool
            空の場合にTrueが設定される。
        """
        return not self._container

    def push(self, node: Node) -> None:
        """
        キューへのノードのインスタンスの追加を行う。

        Parameters
        ----------
        node : Node
            追加対象のノードのインスタンス。
        """
        heapq.heappush(self._container, node)

    def pop(self) -> Node:
        """
        キューから優先度の一番高いノードのインスタンスを取り出す。

        Returns
        -------
        node : Node
            取り出されたNodeクラスのインスタンス。
        """
        return heapq.heappop(self._container)


def astar(
        maze,
        init_loc: Location,
        is_goal_loc_method: Callable[[Location], bool],
        get_movable_locations_method: Callable[[Location], List[Location]],
        hueristic_method: Callable[[Location], int],
        limit_time
) -> Optional[Node]:
    """
    A*アルゴリズムによる探索処理を行う。

    Parameters
    ----------
    init_loc : Location
        探索開始位置（迷路の入口の位置）。
    is_goal_loc_method : callable
        対象の位置が出口（ゴール）かどうかの判定を行うメソッド。
    get_movable_locations_method : callable
        対象の位置からの移動先のセルの位置のリストを取得するメソッド。
    hueristic_method : callable
        対象の位置から出口（ゴール）までの位置の間の距離を取得する
        ためのヒューリスティック用のメソッド。

    Returns
    -------
    goal_node : Node or None
        算出された出口の位置のノードのインスタンス。出口までの
        経路が算出できないケースではNoneが設定される。
    """
    frontier_queue: PriorityQueue = PriorityQueue()
    begin_time = time()
    frontier_queue.push(
        node=Node(
            location=init_loc,
            parent=None,
            cost=0,
            heuristic=hueristic_method(init_loc)))

    explored_loc_cost_dict: Dict[Location, float] = {init_loc: 0.0}

    while not frontier_queue.empty:
        # No Limit Time
        # if time() - begin_time > limit_time:
        #     print('time over')
        #     break
        current_node: Node = frontier_queue.pop()
        current_loc: Location = current_node.location

        if is_goal_loc_method(current_loc):
            return current_node

        movable_locations = get_movable_locations_method(current_loc)
        for movable_location in movable_locations:
            key = (current_loc.row, current_loc.column, movable_location.row, movable_location.column)
            if key in maze.height_dict:
                h_cost = maze.height_dict[key]
                new_cost: float = current_node.cost + h_cost
            else:
                h_cost = abs(
                    maze.height_map[movable_location.row][movable_location.column] - maze.height_map[current_loc.row][
                        current_loc.column])
                new_cost: float = current_node.cost + h_cost
                maze.height_dict[key] = h_cost
            
            if maze.area_map[movable_location.row][movable_location.column] == 2:
                new_cost += 10

            # 新しい移動先が既に探索済みで、且つコスト的にも優位ではない
            # 場合にはスキップする。
            if (movable_location in explored_loc_cost_dict and
                    explored_loc_cost_dict[movable_location] <= new_cost):
                continue

            explored_loc_cost_dict[movable_location] = new_cost
            frontier_queue.push(
                node=Node(
                    location=movable_location,
                    parent=current_node,
                    cost=new_cost,
                    heuristic=hueristic_method(movable_location)))
    return None


def make_maze(heightmap, area_with_border):
    return Maze(heightmap, area_with_border)


def set_star_end(maze, start, end):
    maze.set_start_and_goal_location(start, end)


def run(maze):
    goal_node: Optional[Node] = astar(
        maze,
        init_loc=maze.start_loc,
        is_goal_loc_method=maze.is_goal_loc,
        get_movable_locations_method=maze.get_movable_locations,
        hueristic_method=maze.get_manhattan_distance,
        limit_time=30.0
    )
    if goal_node is None:
        print('time over or 出口が算出できない迷路です。')
        return []
    else:
        # print('-' * 20)
        path = get_path_from_goal_node(goal_node=goal_node)
        return path
