from django.shortcuts import render, get_object_or_404, redirect
from .models import Game

def home(request):
    games = Game.objects.all()
    return render(request, 'game/home.html', {'games': games})

def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    
    if request.method == 'POST' and not game.is_over:
        position = int(request.POST.get('position'))
        # Convert position to index in the flat string
        if 0 <= position < 9:
            if game.board[position] == ' ':
                row = position // 3
                col = position % 3
                game.make_move(row, col)
                
                winner = game.check_winner()
                if winner:
                    game.is_over = True
                    game.winner = winner if winner != 'D' else None
                    game.save()
    
    return render(request, 'game/game.html', {'game': game})

def new_game(request):
    game = Game.objects.create()
    return redirect('game', game_id=game.id) 