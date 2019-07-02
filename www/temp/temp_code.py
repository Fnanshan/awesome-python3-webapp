# coding=utf-8
# board opt
@app.route('/query_board', methods=['GET', 'POST'])
def query_board():
    board = system.Board()
    if request.method == 'POST':
        return render_template('board.html')
    # get操作，先获取数据库中的board
    # query_board_sql = 'select * from board;'
    result = board.query_board()
    return render_template('board.html', result=result, len_result=len(result))


@app.route('/save_board', methods=['GET', 'POST'])
def save_board():
    board = system.Board()
    if request.method == 'POST':
        update_board_sql = ''
        # result = board.update_board(update_board)
        return request.args
    return request.args