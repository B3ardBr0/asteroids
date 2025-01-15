# Asteroids Game

A Python implementation of the classic arcade game Asteroids using Pygame.

## Description

In this version of Asteroids, you control a spaceship in a field of asteroids. Your goal is to survive as long as possible while shooting asteroids to earn points. The game features:

- Player spaceship with full movement controls
- Shooting mechanics with cooldown
- Asteroids that split into smaller pieces when shot
- Particle explosion effects
- Lives system with respawning
- Score tracking
- Start menu
- Screen wrapping for all game objects

## Controls

- W: Move forward
- S: Move backward
- A: Rotate left
- D: Rotate right
- SPACE: Shoot
- SPACE (in menu): Start game

## Features

### Scoring System
- Large Asteroid: 20 points
- Medium Asteroid: 50 points
- Small Asteroid: 100 points

### Player
- 3 lives to start
- Temporary invulnerability after respawning
- Visual feedback (flashing) during invulnerability period

### Gameplay Mechanics
- Asteroids split into smaller pieces when shot
- All objects wrap around screen edges
- Particle effects when asteroids are destroyed
