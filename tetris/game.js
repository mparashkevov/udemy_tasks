/**
 * TETRIS NEON EDITION
 * A premium Tetris game with stunning visuals
 */

// ============================================
// TETROMINO DEFINITIONS
// ============================================
const TETROMINOS = {
    I: {
        shape: [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        color: '#00f5ff',
        shadowColor: 'rgba(0, 245, 255, 0.5)'
    },
    O: {
        shape: [
            [1, 1],
            [1, 1]
        ],
        color: '#ffee00',
        shadowColor: 'rgba(255, 238, 0, 0.5)'
    },
    T: {
        shape: [
            [0, 1, 0],
            [1, 1, 1],
            [0, 0, 0]
        ],
        color: '#bf00ff',
        shadowColor: 'rgba(191, 0, 255, 0.5)'
    },
    S: {
        shape: [
            [0, 1, 1],
            [1, 1, 0],
            [0, 0, 0]
        ],
        color: '#00ff88',
        shadowColor: 'rgba(0, 255, 136, 0.5)'
    },
    Z: {
        shape: [
            [1, 1, 0],
            [0, 1, 1],
            [0, 0, 0]
        ],
        color: '#ff0055',
        shadowColor: 'rgba(255, 0, 85, 0.5)'
    },
    J: {
        shape: [
            [1, 0, 0],
            [1, 1, 1],
            [0, 0, 0]
        ],
        color: '#0066ff',
        shadowColor: 'rgba(0, 102, 255, 0.5)'
    },
    L: {
        shape: [
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]
        ],
        color: '#ff8800',
        shadowColor: 'rgba(255, 136, 0, 0.5)'
    }
};

// Wall kick data for SRS (Super Rotation System)
const WALL_KICKS = {
    'JLSTZ': {
        '0>1': [[-1, 0], [-1, 1], [0, -2], [-1, -2]],
        '1>0': [[1, 0], [1, -1], [0, 2], [1, 2]],
        '1>2': [[1, 0], [1, -1], [0, 2], [1, 2]],
        '2>1': [[-1, 0], [-1, 1], [0, -2], [-1, -2]],
        '2>3': [[1, 0], [1, 1], [0, -2], [1, -2]],
        '3>2': [[-1, 0], [-1, -1], [0, 2], [-1, 2]],
        '3>0': [[-1, 0], [-1, -1], [0, 2], [-1, 2]],
        '0>3': [[1, 0], [1, 1], [0, -2], [1, -2]]
    },
    'I': {
        '0>1': [[-2, 0], [1, 0], [-2, -1], [1, 2]],
        '1>0': [[2, 0], [-1, 0], [2, 1], [-1, -2]],
        '1>2': [[-1, 0], [2, 0], [-1, 2], [2, -1]],
        '2>1': [[1, 0], [-2, 0], [1, -2], [-2, 1]],
        '2>3': [[2, 0], [-1, 0], [2, 1], [-1, -2]],
        '3>2': [[-2, 0], [1, 0], [-2, -1], [1, 2]],
        '3>0': [[1, 0], [-2, 0], [1, -2], [-2, 1]],
        '0>3': [[-1, 0], [2, 0], [-1, 2], [2, -1]]
    }
};

// ============================================
// GAME CONSTANTS
// ============================================
const BOARD_WIDTH = 10;
const BOARD_HEIGHT = 20;
const CELL_SIZE = 30;
const MINI_CELL_SIZE = 15;

// Scoring
const SCORE_VALUES = {
    SOFT_DROP: 1,
    HARD_DROP: 2,
    SINGLE: 100,
    DOUBLE: 300,
    TRIPLE: 500,
    TETRIS: 800
};

// Level speeds (ms per drop)
const LEVEL_SPEEDS = [
    1000, 900, 800, 700, 600, 500, 400, 300, 200, 100,
    90, 80, 70, 60, 50, 40, 30, 20, 15, 10
];

// ============================================
// GAME STATE
// ============================================
class TetrisGame {
    constructor() {
        // Canvas setup
        this.canvas = document.getElementById('tetris-canvas');
        this.ctx = this.canvas.getContext('2d');

        // DOM elements
        this.overlay = document.getElementById('game-overlay');
        this.overlayTitle = document.getElementById('overlay-title');
        this.overlayMessage = document.getElementById('overlay-message');
        this.startButton = document.getElementById('start-button');
        this.pauseButton = document.getElementById('pause-button');
        this.pauseText = document.getElementById('pause-text');
        this.restartButton = document.getElementById('restart-button');
        this.scoreDisplay = document.getElementById('score');
        this.levelDisplay = document.getElementById('level');
        this.linesDisplay = document.getElementById('lines');
        this.highScoreDisplay = document.getElementById('high-score');
        this.particlesContainer = document.getElementById('particles');

        // Options modal elements
        this.optionsButton = document.getElementById('options-button');
        this.optionsModal = document.getElementById('options-modal');
        this.closeOptionsButton = document.getElementById('close-options');
        this.themeButtons = document.querySelectorAll('.theme-btn');
        this.editionSubtitle = document.getElementById('edition-subtitle');

        // Game state
        this.board = [];
        this.currentPiece = null;
        this.currentPieceType = null;
        this.currentX = 0;
        this.currentY = 0;
        this.currentRotation = 0;
        this.holdPiece = null;
        this.canHold = true;
        this.nextPieces = [];
        this.bag = [];

        // Stats
        this.score = 0;
        this.level = 1;
        this.lines = 0;
        this.highScore = parseInt(localStorage.getItem('tetrisHighScore')) || 0;

        // Game flags
        this.isPlaying = false;
        this.isPaused = false;
        this.isGameOver = false;
        this.lockDelay = false;
        this.lockDelayTimer = null;

        // Timers
        this.dropTimer = null;
        this.lastTime = 0;
        this.dropInterval = LEVEL_SPEEDS[0];

        // Theme state
        this.currentTheme = localStorage.getItem('tetrisTheme') || 'neon';

        // Initialize
        this.init();
    }

    init() {
        this.highScoreDisplay.textContent = this.highScore;
        this.setupEventListeners();
        this.createMiniCanvases();
        this.resetBoard();
        this.applyTheme(this.currentTheme);
        this.draw();
    }

    createMiniCanvases() {
        // Hold canvas
        const holdGrid = document.getElementById('hold-grid');
        holdGrid.innerHTML = '<canvas width="120" height="80"></canvas>';
        this.holdCanvas = holdGrid.querySelector('canvas');
        this.holdCtx = this.holdCanvas.getContext('2d');

        // Next piece canvases
        this.nextCanvases = [];
        this.nextCtxs = [];
        for (let i = 0; i < 3; i++) {
            const grid = document.getElementById(`next-${i}`);
            grid.innerHTML = '<canvas width="120" height="60"></canvas>';
            const canvas = grid.querySelector('canvas');
            this.nextCanvases.push(canvas);
            this.nextCtxs.push(canvas.getContext('2d'));
        }
    }

    setupEventListeners() {
        // Keyboard controls
        document.addEventListener('keydown', (e) => this.handleKeyDown(e));

        // Button controls
        this.startButton.addEventListener('click', () => this.startGame());
        this.pauseButton.addEventListener('click', () => this.togglePause());
        this.restartButton.addEventListener('click', () => this.restartGame());

        // Options modal controls
        this.optionsButton.addEventListener('click', () => this.openOptions());
        this.closeOptionsButton.addEventListener('click', () => this.closeOptions());
        this.optionsModal.addEventListener('click', (e) => {
            if (e.target === this.optionsModal) this.closeOptions();
        });

        // Theme buttons
        this.themeButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                const theme = btn.dataset.theme;
                this.applyTheme(theme);
            });
        });
    }

    handleKeyDown(e) {
        // Prevent default for game keys
        const gameKeys = ['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight',
            'Space', 'KeyW', 'KeyA', 'KeyS', 'KeyD', 'KeyZ',
            'KeyP', 'KeyR', 'ShiftLeft', 'ShiftRight', 'KeyC', 'Enter'];
        if (gameKeys.includes(e.code)) {
            e.preventDefault();
        }

        // Start game with Enter
        if (e.code === 'Enter' && !this.isPlaying) {
            this.startGame();
            return;
        }

        // Pause with P
        if (e.code === 'KeyP') {
            this.togglePause();
            return;
        }

        // Restart with R
        if (e.code === 'KeyR') {
            this.restartGame();
            return;
        }

        // Only process game controls if playing and not paused
        if (!this.isPlaying || this.isPaused || this.isGameOver) return;

        switch (e.code) {
            case 'ArrowLeft':
            case 'KeyA':
                this.movePiece(-1, 0);
                break;
            case 'ArrowRight':
            case 'KeyD':
                this.movePiece(1, 0);
                break;
            case 'ArrowDown':
            case 'KeyS':
                this.softDrop();
                break;
            case 'ArrowUp':
            case 'KeyW':
                this.rotatePiece(1);
                break;
            case 'KeyZ':
                this.rotatePiece(-1);
                break;
            case 'Space':
                this.hardDrop();
                break;
            case 'ShiftLeft':
            case 'ShiftRight':
            case 'KeyC':
                this.holdCurrentPiece();
                break;
        }
    }

    // ========================================
    // GAME FLOW
    // ========================================

    startGame() {
        this.resetBoard();
        this.score = 0;
        this.level = 1;
        this.lines = 0;
        this.holdPiece = null;
        this.canHold = true;
        this.bag = [];
        this.nextPieces = [];
        this.isPlaying = true;
        this.isPaused = false;
        this.isGameOver = false;

        this.updateStats();
        this.hideOverlay();
        this.fillNextPieces();
        this.spawnPiece();
        this.startDropTimer();
    }

    restartGame() {
        this.stopDropTimer();
        this.startGame();
    }

    togglePause() {
        if (!this.isPlaying || this.isGameOver) return;

        this.isPaused = !this.isPaused;
        this.pauseText.textContent = this.isPaused ? 'RESUME' : 'PAUSE';

        if (this.isPaused) {
            this.stopDropTimer();
            this.showOverlay('PAUSED', 'Press P to Resume');
        } else {
            this.hideOverlay();
            this.startDropTimer();
        }
    }

    gameOver() {
        this.isGameOver = true;
        this.isPlaying = false;
        this.stopDropTimer();

        // Update high score
        if (this.score > this.highScore) {
            this.highScore = this.score;
            localStorage.setItem('tetrisHighScore', this.highScore);
            this.highScoreDisplay.textContent = this.highScore;
        }

        this.showOverlay('GAME OVER', `Final Score: ${this.score}`);
        this.startButton.textContent = 'PLAY AGAIN';
    }

    showOverlay(title, message) {
        this.overlayTitle.textContent = title;
        this.overlayMessage.textContent = message;
        this.overlay.classList.remove('hidden');
    }

    hideOverlay() {
        this.overlay.classList.add('hidden');
    }

    // ========================================
    // OPTIONS & THEMES
    // ========================================

    openOptions() {
        this.optionsModal.classList.remove('hidden');
        // Pause game if playing
        if (this.isPlaying && !this.isPaused) {
            this.togglePause();
        }
    }

    closeOptions() {
        this.optionsModal.classList.add('hidden');
    }

    applyTheme(themeName) {
        // Remove all theme classes
        document.body.classList.remove('theme-neon', 'theme-metal', 'theme-wood');

        // Apply new theme class (neon is default, no class needed)
        if (themeName !== 'neon') {
            document.body.classList.add(`theme-${themeName}`);
        }

        // Update theme button active states
        this.themeButtons.forEach(btn => {
            btn.classList.toggle('active', btn.dataset.theme === themeName);
        });

        // Update subtitle
        const themeNames = {
            'neon': 'NEON EDITION',
            'metal': 'METAL EDITION',
            'wood': 'WOOD EDITION'
        };
        this.editionSubtitle.textContent = themeNames[themeName];

        // Update tetromino colors based on theme
        this.updateTetrominoColors(themeName);

        // Save theme preference
        this.currentTheme = themeName;
        localStorage.setItem('tetrisTheme', themeName);

        // Redraw to apply new colors
        this.draw();
        this.drawHoldPiece();
        this.drawNextPieces();
    }

    updateTetrominoColors(themeName) {
        const themes = {
            'neon': {
                I: { color: '#00f5ff', shadowColor: '#00a0aa' },
                O: { color: '#ffee00', shadowColor: '#aa9900' },
                T: { color: '#bf00ff', shadowColor: '#8000aa' },
                S: { color: '#00ff88', shadowColor: '#00aa55' },
                Z: { color: '#ff0055', shadowColor: '#aa0033' },
                J: { color: '#0066ff', shadowColor: '#0044aa' },
                L: { color: '#ff8800', shadowColor: '#aa5500' }
            },
            'metal': {
                I: { color: '#a8c0d3', shadowColor: '#6080a0' },
                O: { color: '#c9b037', shadowColor: '#908020' },
                T: { color: '#8e8e8e', shadowColor: '#555555' },
                S: { color: '#7a9b76', shadowColor: '#506850' },
                Z: { color: '#b85450', shadowColor: '#803530' },
                J: { color: '#5a6a8a', shadowColor: '#354060' },
                L: { color: '#c87533', shadowColor: '#905020' }
            },
            'wood': {
                I: { color: '#7cb3a8', shadowColor: '#508070' },
                O: { color: '#e6c86e', shadowColor: '#a08840' },
                T: { color: '#9b6b9e', shadowColor: '#604565' },
                S: { color: '#7a9b60', shadowColor: '#506540' },
                Z: { color: '#c45c4a', shadowColor: '#803530' },
                J: { color: '#4a6889', shadowColor: '#304560' },
                L: { color: '#d4924a', shadowColor: '#906030' }
            }
        };

        const themeColors = themes[themeName] || themes.neon;

        // Update TETROMINOS object with new colors
        Object.keys(themeColors).forEach(piece => {
            if (TETROMINOS[piece]) {
                TETROMINOS[piece].color = themeColors[piece].color;
                TETROMINOS[piece].shadowColor = themeColors[piece].shadowColor;
            }
        });
    }

    // ========================================
    // BOARD MANAGEMENT
    // ========================================

    resetBoard() {
        this.board = Array(BOARD_HEIGHT).fill(null).map(() =>
            Array(BOARD_WIDTH).fill(null)
        );
    }

    // ========================================
    // PIECE GENERATION (7-Bag System)
    // ========================================

    shuffleBag() {
        const pieces = Object.keys(TETROMINOS);
        // Fisher-Yates shuffle
        for (let i = pieces.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [pieces[i], pieces[j]] = [pieces[j], pieces[i]];
        }
        return pieces;
    }

    getNextPieceType() {
        if (this.bag.length === 0) {
            this.bag = this.shuffleBag();
        }
        return this.bag.pop();
    }

    fillNextPieces() {
        while (this.nextPieces.length < 3) {
            this.nextPieces.push(this.getNextPieceType());
        }
        this.drawNextPieces();
    }

    spawnPiece() {
        this.currentPieceType = this.nextPieces.shift();
        this.fillNextPieces();

        this.currentPiece = TETROMINOS[this.currentPieceType].shape.map(row => [...row]);
        this.currentRotation = 0;
        this.currentX = Math.floor((BOARD_WIDTH - this.currentPiece[0].length) / 2);
        this.currentY = 0;
        this.canHold = true;

        // Check if spawn position is valid
        if (!this.isValidPosition(this.currentX, this.currentY, this.currentPiece)) {
            this.gameOver();
        }

        this.draw();
    }

    // ========================================
    // PIECE MOVEMENT & ROTATION
    // ========================================

    movePiece(dx, dy) {
        const newX = this.currentX + dx;
        const newY = this.currentY + dy;

        if (this.isValidPosition(newX, newY, this.currentPiece)) {
            this.currentX = newX;
            this.currentY = newY;
            this.draw();

            // Reset lock delay if moving
            if (this.lockDelay && dy === 0) {
                this.resetLockDelay();
            }
            return true;
        }
        return false;
    }

    rotatePiece(direction) {
        const rotated = this.getRotatedPiece(direction);
        const newRotation = (this.currentRotation + direction + 4) % 4;

        // Try basic rotation
        if (this.isValidPosition(this.currentX, this.currentY, rotated)) {
            this.currentPiece = rotated;
            this.currentRotation = newRotation;
            this.draw();
            if (this.lockDelay) this.resetLockDelay();
            return true;
        }

        // Try wall kicks
        const kickData = this.currentPieceType === 'I' ? WALL_KICKS.I : WALL_KICKS.JLSTZ;
        const kickKey = `${this.currentRotation}>${newRotation}`;
        const kicks = kickData[kickKey] || [];

        for (const [kickX, kickY] of kicks) {
            if (this.isValidPosition(this.currentX + kickX, this.currentY - kickY, rotated)) {
                this.currentX += kickX;
                this.currentY -= kickY;
                this.currentPiece = rotated;
                this.currentRotation = newRotation;
                this.draw();
                if (this.lockDelay) this.resetLockDelay();
                return true;
            }
        }

        return false;
    }

    getRotatedPiece(direction) {
        const piece = this.currentPiece;
        const size = piece.length;
        const rotated = Array(size).fill(null).map(() => Array(size).fill(0));

        for (let y = 0; y < size; y++) {
            for (let x = 0; x < size; x++) {
                if (direction === 1) {
                    // Clockwise
                    rotated[x][size - 1 - y] = piece[y][x];
                } else {
                    // Counter-clockwise
                    rotated[size - 1 - x][y] = piece[y][x];
                }
            }
        }

        return rotated;
    }

    // ========================================
    // COLLISION DETECTION
    // ========================================

    isValidPosition(x, y, piece) {
        for (let py = 0; py < piece.length; py++) {
            for (let px = 0; px < piece[py].length; px++) {
                if (piece[py][px]) {
                    const boardX = x + px;
                    const boardY = y + py;

                    // Check boundaries
                    if (boardX < 0 || boardX >= BOARD_WIDTH ||
                        boardY < 0 || boardY >= BOARD_HEIGHT) {
                        return false;
                    }

                    // Check collision with placed pieces
                    if (this.board[boardY][boardX]) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    // ========================================
    // DROP MECHANICS
    // ========================================

    startDropTimer() {
        this.stopDropTimer();
        this.dropInterval = LEVEL_SPEEDS[Math.min(this.level - 1, LEVEL_SPEEDS.length - 1)];

        const drop = () => {
            if (!this.isPaused && this.isPlaying && !this.isGameOver) {
                this.dropPiece();
            }
            this.dropTimer = setTimeout(drop, this.dropInterval);
        };

        this.dropTimer = setTimeout(drop, this.dropInterval);
    }

    stopDropTimer() {
        if (this.dropTimer) {
            clearTimeout(this.dropTimer);
            this.dropTimer = null;
        }
        if (this.lockDelayTimer) {
            clearTimeout(this.lockDelayTimer);
            this.lockDelayTimer = null;
        }
    }

    dropPiece() {
        if (!this.movePiece(0, 1)) {
            // Piece can't move down, start lock delay
            if (!this.lockDelay) {
                this.startLockDelay();
            }
        } else {
            this.lockDelay = false;
        }
    }

    startLockDelay() {
        this.lockDelay = true;
        this.lockDelayTimer = setTimeout(() => {
            if (this.lockDelay) {
                this.lockPiece();
            }
        }, 500);
    }

    resetLockDelay() {
        if (this.lockDelayTimer) {
            clearTimeout(this.lockDelayTimer);
        }
        this.startLockDelay();
    }

    softDrop() {
        if (this.movePiece(0, 1)) {
            this.score += SCORE_VALUES.SOFT_DROP;
            this.updateStats();
        }
    }

    hardDrop() {
        let dropDistance = 0;
        while (this.movePiece(0, 1)) {
            dropDistance++;
        }
        this.score += dropDistance * SCORE_VALUES.HARD_DROP;
        this.updateStats();
        this.lockPiece();
    }

    // ========================================
    // PIECE LOCKING & LINE CLEARING
    // ========================================

    lockPiece() {
        this.lockDelay = false;
        if (this.lockDelayTimer) {
            clearTimeout(this.lockDelayTimer);
            this.lockDelayTimer = null;
        }

        // Place piece on board
        for (let py = 0; py < this.currentPiece.length; py++) {
            for (let px = 0; px < this.currentPiece[py].length; px++) {
                if (this.currentPiece[py][px]) {
                    const boardY = this.currentY + py;
                    const boardX = this.currentX + px;
                    if (boardY >= 0) {
                        this.board[boardY][boardX] = {
                            color: TETROMINOS[this.currentPieceType].color,
                            shadowColor: TETROMINOS[this.currentPieceType].shadowColor
                        };
                    }
                }
            }
        }

        // Check for line clears
        this.checkLines();

        // Spawn next piece
        this.spawnPiece();
    }

    checkLines() {
        const linesToClear = [];

        for (let y = BOARD_HEIGHT - 1; y >= 0; y--) {
            if (this.board[y].every(cell => cell !== null)) {
                linesToClear.push(y);
            }
        }

        if (linesToClear.length > 0) {
            this.clearLines(linesToClear);
        }
    }

    clearLines(lines) {
        // Create particles for line clear effect
        lines.forEach(y => {
            this.createLineClearParticles(y);
        });

        // Calculate score
        const lineScores = [0, SCORE_VALUES.SINGLE, SCORE_VALUES.DOUBLE,
            SCORE_VALUES.TRIPLE, SCORE_VALUES.TETRIS];
        const scoreMultiplier = Math.min(lines.length, 4);
        const points = lineScores[scoreMultiplier] * this.level;

        this.score += points;
        this.lines += lines.length;

        // Show score popup
        this.showScorePopup(points);

        // Level up every 10 lines
        const newLevel = Math.floor(this.lines / 10) + 1;
        if (newLevel > this.level) {
            this.level = newLevel;
            this.dropInterval = LEVEL_SPEEDS[Math.min(this.level - 1, LEVEL_SPEEDS.length - 1)];
        }

        // Remove cleared lines - build new board to avoid index shifting issues
        const newBoard = [];
        for (let y = 0; y < BOARD_HEIGHT; y++) {
            if (!lines.includes(y)) {
                newBoard.push(this.board[y]);
            }
        }
        // Add empty rows at the top
        while (newBoard.length < BOARD_HEIGHT) {
            newBoard.unshift(Array(BOARD_WIDTH).fill(null));
        }
        this.board = newBoard;

        this.updateStats();
        this.draw();
    }

    // ========================================
    // HOLD PIECE
    // ========================================

    holdCurrentPiece() {
        if (!this.canHold) return;

        const currentType = this.currentPieceType;

        if (this.holdPiece) {
            // Swap with held piece
            this.currentPieceType = this.holdPiece;
            this.holdPiece = currentType;

            this.currentPiece = TETROMINOS[this.currentPieceType].shape.map(row => [...row]);
            this.currentRotation = 0;
            this.currentX = Math.floor((BOARD_WIDTH - this.currentPiece[0].length) / 2);
            this.currentY = 0;
        } else {
            // Hold current piece, spawn new one
            this.holdPiece = currentType;
            this.spawnPiece();
        }

        this.canHold = false;
        this.drawHoldPiece();
        this.draw();
    }

    // ========================================
    // GHOST PIECE
    // ========================================

    getGhostY() {
        let ghostY = this.currentY;
        while (this.isValidPosition(this.currentX, ghostY + 1, this.currentPiece)) {
            ghostY++;
        }
        return ghostY;
    }

    // ========================================
    // RENDERING
    // ========================================

    draw() {
        // Clear canvas
        this.ctx.fillStyle = 'rgba(10, 10, 30, 0.9)';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        // Draw grid
        this.drawGrid();

        // Draw placed pieces
        this.drawBoard();

        // Draw ghost piece
        if (this.currentPiece) {
            this.drawGhostPiece();
        }

        // Draw current piece
        if (this.currentPiece) {
            this.drawCurrentPiece();
        }
    }

    drawGrid() {
        this.ctx.strokeStyle = 'rgba(100, 100, 255, 0.1)';
        this.ctx.lineWidth = 1;

        for (let x = 0; x <= BOARD_WIDTH; x++) {
            this.ctx.beginPath();
            this.ctx.moveTo(x * CELL_SIZE, 0);
            this.ctx.lineTo(x * CELL_SIZE, BOARD_HEIGHT * CELL_SIZE);
            this.ctx.stroke();
        }

        for (let y = 0; y <= BOARD_HEIGHT; y++) {
            this.ctx.beginPath();
            this.ctx.moveTo(0, y * CELL_SIZE);
            this.ctx.lineTo(BOARD_WIDTH * CELL_SIZE, y * CELL_SIZE);
            this.ctx.stroke();
        }
    }

    drawBoard() {
        for (let y = 0; y < BOARD_HEIGHT; y++) {
            for (let x = 0; x < BOARD_WIDTH; x++) {
                if (this.board[y][x]) {
                    this.drawCell(x, y, this.board[y][x].color, this.board[y][x].shadowColor);
                }
            }
        }
    }

    drawCurrentPiece() {
        const { color, shadowColor } = TETROMINOS[this.currentPieceType];

        for (let py = 0; py < this.currentPiece.length; py++) {
            for (let px = 0; px < this.currentPiece[py].length; px++) {
                if (this.currentPiece[py][px]) {
                    this.drawCell(
                        this.currentX + px,
                        this.currentY + py,
                        color,
                        shadowColor
                    );
                }
            }
        }
    }

    drawGhostPiece() {
        const ghostY = this.getGhostY();
        if (ghostY === this.currentY) return;

        const { color } = TETROMINOS[this.currentPieceType];

        for (let py = 0; py < this.currentPiece.length; py++) {
            for (let px = 0; px < this.currentPiece[py].length; px++) {
                if (this.currentPiece[py][px]) {
                    const x = (this.currentX + px) * CELL_SIZE;
                    const y = (ghostY + py) * CELL_SIZE;

                    this.ctx.strokeStyle = color;
                    this.ctx.lineWidth = 2;
                    this.ctx.globalAlpha = 0.3;
                    this.ctx.strokeRect(x + 2, y + 2, CELL_SIZE - 4, CELL_SIZE - 4);
                    this.ctx.globalAlpha = 1;
                }
            }
        }
    }

    drawCell(cellX, cellY, color, shadowColor) {
        const x = cellX * CELL_SIZE;
        const y = cellY * CELL_SIZE;
        const padding = 2;

        // Glow effect
        this.ctx.shadowColor = shadowColor;
        this.ctx.shadowBlur = 10;

        // Main cell
        const gradient = this.ctx.createLinearGradient(x, y, x + CELL_SIZE, y + CELL_SIZE);
        gradient.addColorStop(0, color);
        gradient.addColorStop(1, this.adjustBrightness(color, -30));

        this.ctx.fillStyle = gradient;
        this.ctx.fillRect(x + padding, y + padding, CELL_SIZE - padding * 2, CELL_SIZE - padding * 2);

        // Inner highlight
        this.ctx.fillStyle = 'rgba(255, 255, 255, 0.3)';
        this.ctx.fillRect(x + padding + 2, y + padding + 2, CELL_SIZE - padding * 2 - 4, 4);

        // Border
        this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.5)';
        this.ctx.lineWidth = 1;
        this.ctx.strokeRect(x + padding, y + padding, CELL_SIZE - padding * 2, CELL_SIZE - padding * 2);

        // Reset shadow
        this.ctx.shadowBlur = 0;
    }

    adjustBrightness(color, percent) {
        const num = parseInt(color.slice(1), 16);
        const r = Math.max(0, Math.min(255, (num >> 16) + percent));
        const g = Math.max(0, Math.min(255, ((num >> 8) & 0x00FF) + percent));
        const b = Math.max(0, Math.min(255, (num & 0x0000FF) + percent));
        return `#${((r << 16) | (g << 8) | b).toString(16).padStart(6, '0')}`;
    }

    // ========================================
    // MINI DISPLAYS
    // ========================================

    drawHoldPiece() {
        this.holdCtx.clearRect(0, 0, this.holdCanvas.width, this.holdCanvas.height);

        if (!this.holdPiece) return;

        const tetromino = TETROMINOS[this.holdPiece];
        const shape = tetromino.shape;
        const cellSize = MINI_CELL_SIZE;

        // Center the piece
        const offsetX = (this.holdCanvas.width - shape[0].length * cellSize) / 2;
        const offsetY = (this.holdCanvas.height - shape.length * cellSize) / 2;

        this.drawMiniPiece(this.holdCtx, shape, tetromino.color, tetromino.shadowColor, offsetX, offsetY, cellSize);
    }

    drawNextPieces() {
        this.nextPieces.forEach((pieceType, index) => {
            const ctx = this.nextCtxs[index];
            const canvas = this.nextCanvases[index];

            ctx.clearRect(0, 0, canvas.width, canvas.height);

            const tetromino = TETROMINOS[pieceType];
            const shape = tetromino.shape;
            const cellSize = MINI_CELL_SIZE;

            const offsetX = (canvas.width - shape[0].length * cellSize) / 2;
            const offsetY = (canvas.height - shape.length * cellSize) / 2;

            this.drawMiniPiece(ctx, shape, tetromino.color, tetromino.shadowColor, offsetX, offsetY, cellSize);
        });
    }

    drawMiniPiece(ctx, shape, color, shadowColor, offsetX, offsetY, cellSize) {
        ctx.shadowColor = shadowColor;
        ctx.shadowBlur = 5;

        for (let py = 0; py < shape.length; py++) {
            for (let px = 0; px < shape[py].length; px++) {
                if (shape[py][px]) {
                    const x = offsetX + px * cellSize;
                    const y = offsetY + py * cellSize;

                    const gradient = ctx.createLinearGradient(x, y, x + cellSize, y + cellSize);
                    gradient.addColorStop(0, color);
                    gradient.addColorStop(1, this.adjustBrightness(color, -30));

                    ctx.fillStyle = gradient;
                    ctx.fillRect(x + 1, y + 1, cellSize - 2, cellSize - 2);

                    ctx.fillStyle = 'rgba(255, 255, 255, 0.3)';
                    ctx.fillRect(x + 2, y + 2, cellSize - 4, 2);
                }
            }
        }

        ctx.shadowBlur = 0;
    }

    // ========================================
    // EFFECTS
    // ========================================

    createLineClearParticles(lineY) {
        const y = lineY * CELL_SIZE;
        const particleCount = 20;

        for (let i = 0; i < particleCount; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = `${Math.random() * BOARD_WIDTH * CELL_SIZE + this.canvas.offsetLeft}px`;
            particle.style.top = `${y + this.canvas.offsetTop}px`;
            particle.style.backgroundColor = ['#00f5ff', '#ff00aa', '#ffee00', '#00ff88'][Math.floor(Math.random() * 4)];
            particle.style.boxShadow = `0 0 6px ${particle.style.backgroundColor}`;

            this.particlesContainer.appendChild(particle);

            setTimeout(() => particle.remove(), 1000);
        }
    }

    showScorePopup(points) {
        const popup = document.createElement('div');
        popup.className = 'score-popup';
        popup.textContent = `+${points}`;
        popup.style.left = '50%';
        popup.style.top = '50%';
        popup.style.transform = 'translate(-50%, -50%)';

        const boardContainer = document.querySelector('.game-board');
        boardContainer.appendChild(popup);

        setTimeout(() => popup.remove(), 1000);
    }

    // ========================================
    // STATS
    // ========================================

    updateStats() {
        this.scoreDisplay.textContent = this.score.toLocaleString();
        this.levelDisplay.textContent = this.level;
        this.linesDisplay.textContent = this.lines;
    }
}

// ============================================
// INITIALIZE GAME
// ============================================
const game = new TetrisGame();
