import express from "express";
import { filterEpisodes } from '../controllers/episodeController.js';

const router = express.Router();

router.get('/episodes', filterEpisodes);

export default router;
