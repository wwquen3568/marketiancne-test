from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest

from document.models import Board
from document.forms import BoardForm



# 게시판 조회
def board_read(request):
    boards = Board.objects.all()
    return render(request, 'document/read.html', {'boards': boards})


# 게시판 상세 조회
def board_detail(request, pk):
    board = get_object_or_404(Board, pk=pk)
    board.views += 1  # 조회수 증가
    board.save()
    return render(request, 'document/read_detail.html', {'board': board})


# 게시판 생성
def board_create(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)

        # 유효성 검사
        if form.is_valid():
            form.save()
            return redirect('board_read')

        else:
            return HttpResponseBadRequest()
    
    else:
        form = BoardForm()
        
    return render(request, 'document/create.html', {'form': form})


# 게시판 수정
def board_edit(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            form.save()
            return redirect('board_detail', pk=pk)
        
        else:
            return HttpResponseBadRequest()
    
    else:
        form = BoardForm(instance=board)
    print("결과값:", form)
    return render(request, 'document/edit.html', {'form': form})


# 게시판 삭제
def board_delete(request, pk):
    board = get_object_or_404(Board, pk=pk)
    if request.method == 'POST':
        board.delete()
        return redirect('board_read')
    
    return render(request, 'document/delete.html', {'board': board})
